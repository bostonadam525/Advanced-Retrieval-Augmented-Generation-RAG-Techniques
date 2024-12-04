import streamlit as st
import pandas as pd
from langchain.retrievers import EnsembleRetriever
from langchain.retrievers import BM25Retriever
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceBgeEmbeddings

## load environment
from dotenv import load_dotenv
import os
load_dotenv()
os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY")

import os
os.environ["PYTORCH_DISABLE_PATH_CHECKS"] = "1"

# Title
st.title("Hybrid Search App")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("sampled_data.csv")

data = load_data()

# Initialize BM25 retriever
@st.cache_data
def initialize_bm25_retriever(data):
    return BM25Retriever.from_texts(data["message"].tolist())

bm25_retriever = initialize_bm25_retriever(data)

# Initialize dense retriever
@st.cache_data
def initialize_dense_retriever(data):
    model_name = "BAAI/bge-base-en-v1.5"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True}
    embeddings = HuggingFaceBgeEmbeddings(model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs)
    db = FAISS.from_texts(data["message"].tolist(), embedding=embeddings)
    return db.as_retriever(search_kwargs={"k": 5})

dense_retriever = initialize_dense_retriever(data)

# User input
query = st.text_input("Enter your search query:")

# Initialize state management
if "bm25_weight" not in st.session_state:
    st.session_state.bm25_weight = 0.4

# Weights for BM25 and dense retrieval
bm25_weight = st.slider("Keywords Weight", 0.0, 1.0, st.session_state.bm25_weight, 0.01)
st.session_state.bm25_weight = bm25_weight
dense_weight = 1.0 - bm25_weight

# Number of results
num_results = st.slider("Number of Results", 1, 10, 5)

if query:
    # Initialize ensemble retriever
    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, dense_retriever],
        weights=[st.session_state.bm25_weight, dense_weight]
    )

    # Retrieve relevant documents
    docs = ensemble_retriever.get_relevant_documents(query)[:num_results]

    # Display results
    for doc in docs:
        message_type = data.loc[data["message"] == doc.page_content, "message_type"].values[0]
        message_reason = data.loc[data["message"] == doc.page_content, "message_reason"].values[0]
        st.write(f"Message Type: {message_type}")
        st.write(f"Message Reason: {message_reason}")
        st.write(doc.page_content)
        st.write("---")

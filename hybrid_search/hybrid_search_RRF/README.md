# Hybrid Search application with Reciprocal Rank Fusion

## First steps to set things up (if you already did all this then skip to next section)
1. Create a virtual env: `python -m ven <name of venv>`
2. Activate the venv: `source venv/bin/activate`
    * Note: to stop the virtual environment run this code: `deactivate`
3. pip install packages in the `requirements.txt` file: `pip install -r requirements.txt`
4. Make sure that you have a `.env` file setup with your HUGGINGFACE_API_KEY access token. 
    * This allows you to download and access the embedding models from the hugging face hub. 


## Dataset
* Choose your own dataset. App is designed to work on text right now but future use cases could be multimodal.


# How to run this app

1. Make sure you have all the required dependencies installed. You can install them by running the following command:
    * `pip install -r requirements.txt`

2. Save the Streamlit app code in a Python file, e.g., `hybrid_search_app.py`.

3. Open a terminal or command prompt, navigate to the directory containing the `semantic_awards_app.py` file, and run the following command:
    * `streamlit run hyrbid_search_app.py`
    * This will start the Streamlit server and open your app in a new browser window.

4. If you're running the app for the first time, Streamlit will perform some initial setup and download the required packages. This process may take a few minutes, depending on your internet connection speed.

5. Once the app is running, you should see the "Hybrid Search App" title and the user interface components (text input, sliders, etc.) in your browser.

6. You can interact with the app by entering a search query in the text input field and adjusting the sliders for BM25 weight, dense weight, and the number of results.

7. The app will display the relevant messages based on the search query and the specified weights for BM25 and dense retrieval.

8. If you make any changes to the code in `hybrid_search_app.py` while the app is running, Streamlit will automatically detect the changes and reload the app with the updated code.

9. To stop the Streamlit server, you can press `Ctrl+C` in the terminal or command prompt where the server is running.

# Application Infrastructure

## Embeddings Used
* For this app I used an open source embedding model from Hugging Face.
    * Model: BAAI/bge-base-en-v1.5
    * model_card: https://huggingface.co/BAAI/bge-base-en-v1.5 
 
## Vector Store
* I used the FAISS-CPU vector library from Meta.
* Note, this may have to be upgraded to FAISS-GPU if a larger dataset is used.
 
## System Design Flow
1. User enters search query with keywords or semantic phrase. 
2. Creates embeddings
3. Performs both semantic (dense) and keyword (sparse/BM25 algorithm) retrieval based on:
  * User can set the weight of Keyword vs. Semantic search
  * User can set number of awards to retrieve.
4. Once the messages are retrieved we perform Reciprocal Rank Fusion using the `EnsembleRetriever` from LangChain. 
5. The EnsembleRetriever takes a list of retrievers as input and ensemble that results of each of their retrievals and reranks the results based on the Reciprocal Rank Fusion Algorithm (see above). 
6. RRF is a method for combining multiple result sets with different relevance indicators into a single result set.
  * RRF requires no tuning, and the different relevance indicators do not have to be related to each other to achieve high-quality results.
reference: https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html

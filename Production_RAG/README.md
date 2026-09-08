# Production RAG
- Taking RAG systems to production.
- Anyone can build a RAG POC but can you scale it, optimize it, maintain it, and take it to production? 


---
# Basic RAG Chains

```
## Chain Structure

{context, question} | Prompt     | LLM  | parser
parallel inputs        template    model   output


## Parallel Input Processing

context from corpus <-- retriever

question from user <-- RunnablePassthrough

**Question passes through unchanged


## Prompt Template
- This can vary but usually looks like this:

Answer based only on:
{context}
Question: {question}


```
---
## Handling Outlier questions
- Its paramount that a RAG system needs to be able to say "I don't know" rather than hallucinate or fabricate.
- This involves giving INSTRUCTIONS to the model to do so.
- The common prompt pattern to handle this behavior (it can vary):

```
## The Prompt Pattern

"""Answer ONLY based on the following context.
   If the context doesn't contain the answer, respond with "I don't have enough information to
   give an accurate response to your query.

"""
Context: {context}
Question: {question}
```
- Another way to handle this would be to leverage Guardrails but we will go over that later.

---
## RAG with Citations or Sources
- Its also paramount to not only retrieve the `top_k` most similar or relevant information to a user query, but also to cite the source of the information and to evaluate it.
- Sources/citations MATTER because that way users can verify the system answers and use the citations to make an informative decision on the outputs. It builds trust in your system rather than keeping it as a "black box" it offers an "explainability/interpretability" mode which is user friendly but also a common ethical practice in AI/ML. 
- The common way to do this:

```
## Retriever Output
- Page content here...
- source: doc.pdf, doc.csv

- Additional content...
- source: doc.txt

- FAQ content
- source: faq.md

## To add source tags to each chunk
- we can simply call: `format_docs_with_sources`
- or use a custom function
- or use another library of choice

## Final Formatted Context
[source: doc.pdf]
Page content...

[source: guide.txt]
Additional content...

[source: faq.md]
FAQ content....
```
---
# Document Loaders
- See LangChain docs: https://reference.langchain.com/python/langchain-community/document_loaders
- Typical raw files:
  - pdf
  - txt
  - html
  - docx
  - csv

- LangChain Document Loaders can load these files and create objects:

```
List[Document]
- `page_content` -- the actual text content
- `metadata` -- source, page, author, etc...



```
## Core Document Loaders in LangChain
- PyPDFLoader -- PDF files
- TextLoader -- Plain text
- DirectoryLoader -- multiple files stored in a specific directory
- WebBaseLoader -- web pages
- UnstructuredLoader -- more complex "mixed" document types (e.g. markdown, json, etc.)

- In code this is:

```
## load source document --> init loader function to load the docs
loader = Loader(source) --> docs = loader.load()

```
## PDF loading options
1. **PyPDFLoader**
   - Fast, basic PDF extraction out of the box
   - Speed: Good
   - Metadata: Basic
   - Use case: Simple PDF files
  
2. **PyMuPDFLoader**
   - Fastest, good for metadata
   - Speed: BEST
   - Metadata: RICH
   - Use case: HIGH VOLUME PDF files/workloads
  
3. **UnstructuredPDFLoader**
   - Best for COMPLEX layouts
   - Speed: SLOWER
   - Metadata: DETAILED
   - Use Case: Tables & Layouts

## Web Loading options
1. **Single URL**

```
https://example.com --> WebBaseLoader --> Document
```

2. **Multiple URLs**

```
example.com/page1                        Document[0]
example.com/page2  --> WebBaseLoader --> Document[1]
example.com/page3                        Document[2]

```
## Directory Loading
- Example -- load an entire directory of files:

```
docs/
   report.pdf
   notes.txt                 DirectoryLoader                              Doc report.pdf
   data.csv         --->    path            "docs/"                --->   Doc guide.pdf
   guide.pdf                glob            "**/*.pdf"                    Doc summary.pdf
   readme.txt               loader_cls      PyPDFLoader
   summary.pdf
```
- The glob pattern filters the files. We use `"**/*.pdf"=all` for PDFs in all subdirectories. 

---
# Document Processing Pipelines - RAG Indexing pipelines
- Standard document processing pipeline is as follows:

1. **Document Loaders**
   - Extract text from files or documents
   - Handle various file formats

2. **Text Splitters**
   - Chunking of text into character pieces (e.g. 500-1000 depending upon your data)
   - Preserve sentence boundaries (unless semantic chunking?)
   - Add recursive overlap (100-200 chars) -- debatable as to how effective this can be as it can cause duplicate data and confuse semantics.
     - Overlap goal is to preserve the meaning and "bridge" information between chunks --- however, metadata is helpful with this.
   - Chunking approaches to consider:
     - a. Fixed size
     - b. Semantic
     - c. Document structure
     - d. Hybrid (structure + refinement)
     - e. Recursive
     - f. Recursive with hierachy (parent-child chunks):
       - Parent chunks capture broad context — entire sections or chapters that give the big picture. These might be 2,000–3,000 tokens.
       - Child chunks within each parent provide specific details — individual subsections, examples, or code blocks. These might be 400–800 tokens.
     - g. Metadata - this is similar to above but assigns granular metadata tags to chunk sections for improved retrieval.


3. **Embedding Generation**
   - Convert chunks --> vectors
   - Use foundation model APIs or open source embeddings
  
4. **Vector Storage**
   - Store in vector store or vector DB (e.g. chroma, pinecone, weaviate, faiss)
   - Index for faster efficient search
  
5. **Queries**

---
## Good vs. Bad Chunking == Makes or Breaks your RAG application
- Fixed size chunking --> often rigid and brittle
- **Semantic chunking** --> more dynamic, less brittle, splits at "meaning" boundaries, but can be expensive!


### Why does chunking matter so much?
- Each chunk is embedded in its own vector space in isolation.
- This is the typical chunking pipeline:

```
chunk --> Embedding model --> [incomplete meaning]

**Problem: model only sees fragments, NOT the whole concept**
```
- **Important insight**
  - If the chunks are embedded in isolation --> the embeddings are thus incomplete and lack complete meaning and relationships to other chunks.
  - A user query needs COMPMLETE concepts.
  - **MISMATCH == Poor retrieval == Poor answers**

---
## FOUR Chunking Variables affecting quality
- **KEY INSIGHT: Chunking is NOT actually preprocessing, it is a fundamental cornerstone of your RAG architecture!**

### 1. Chunk size
- Too small? Loses context -- too granular!
- Too large? Dilutes meaning -- duplicate data, costs more $$$$ to embed and store
- "Sweet spot": 200-1000 tokens (depends on your data though....) 

### 2. Overlap
- 10-20% overlap preserves context
- [NVIDIA - Finding the Best Chunking Strategy for Accurate AI Responses](https://developer.nvidia.com/blog/finding-the-best-chunking-strategy-for-accurate-ai-responses/)
- [ChromaDB paper - Evaluating Chunking Strategies for Retrieval](https://www.trychroma.com/research/evaluating-chunking)
  - [ChromaDB Chunk Evaluation package](https://github.com/brandonstarxel/chunking_evaluation)


### 3. Split Boundaries
- Fixed --> random splitting (e.g. every `n` char)
- Recursive --> split at paragraph/sentence level
- Semantic --> split at semantic meaning boundaries

### 4. Content Type
- code
- legal
- medical
- markdown
- PDF
- web
- etc...
---
## Chunking Strategies -- Which one should you use?
- One way to think of this is the following:

```
Fixed --> Recursive --> Semantic --> Late (embed first, chunk later)

Basic -->     Intermediate       --> Advanced      

```
### 1. Fixed Size Chunking
- **How it works:** Splits at EXACT intervals (e.g. ever 500-1000 chars)
- **Problems:**
  - Degrades chunk meaning
  - Context loss
  - Poor information retrieval
  - Incomplete sentences and phrases
  - LLM is causal so will see incomplete chunks/phrases/sentences and predict based on its own training probabilities which do not have the same context as your chunks!
- **When to use this?**
  - Quick prototyping/POCs or for very specific use cases for your data.
- **PROS:** Simple, fast, predictable, easy to use out of the box
- **CONS:** meaning and quality are immediately compromised thus leaving the door open to hallucinations, fabrications, and poor retrieval.

### 2. 

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

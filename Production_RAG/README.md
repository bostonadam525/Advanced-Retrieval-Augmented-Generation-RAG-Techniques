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

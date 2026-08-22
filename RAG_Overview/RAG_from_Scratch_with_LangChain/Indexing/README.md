# Indexing
- Important points on Indexing in RAG
---
# Indexing Methods

## Structural & Logical Indexing Strategies

1. Chunk Indexing
2. Sub-chunk indexing
3. Query indexing
4. Summary indexing
5. Hierarchical indexing
6. Hybrid indexing (multi-modal)
7. Multi-representation indexing (multiple embeddings of same chunk)
8. Graph enhanced indexing
9. Time based (e.g. time stamps)

## Vector Database Index Types
1. Flat (Brute-Force): Compares queries against every single vector; highly accurate but slow on large datasets.

2. HNSW (Hierarchical Navigable Small World): Builds multi-layered graphs for fast, highly accurate approximate nearest neighbor searches.

3. IVF (Inverted File Index): Groups vectors into clusters using centroids to narrow search spaces quickly.

4. PQ (Product Quantization): Compresses high-dimensional vectors into smaller sub-vectors to drastically reduce memory usage.

5. LSH (Locality Sensitive Hashing): Hashes similar high-dimensional vectors into localized buckets for rapid retrieval

---
## Overview of Indexing

<img width="973" height="1650" alt="indexing rag" src="https://github.com/user-attachments/assets/c208ddda-20ad-4cb4-b8f1-7e5a7c7a2771" />




---
# Resources
- [chunk viz](https://chunkviz.up.railway.app/)
- [Advanced Indexing Techniques in RAG Systems: Beyond Basic Chunking](https://medium.com/@gauravbansalutd/advanced-indexing-techniques-in-rag-systems-beyond-basic-chunking-ea6a84e4627c)
- [Advanced Indexing Techniques in RAG Systems: Beyond Basic Chunking | Part II](https://medium.com/@gauravbansalutd/advanced-indexing-techniques-in-rag-systems-beyond-basic-chunking-part-ii-0d5e190c7a57)
- [What is RAG Indexing?](https://www.analyticsvidhya.com/blog/2025/11/what-is-rag-indexing/)

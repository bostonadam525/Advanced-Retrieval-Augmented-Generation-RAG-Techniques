# Multimodal RAG with Videos
- A repo devoted to multimodal RAG: Video, Audio, Image, Text, and more. 

---
# Multimodal Embeddings
- Different inputs in a shared vector space.
- These include:

1. Text
2. Image
3. Audio
4. Video

## Embedding Models
- `jinaai/jina-embeddings-v5-omni-small'
  - model card: https://huggingface.co/jinaai/jina-embeddings-v5-omni-small
 
<img width="1774" height="887" alt="image" src="https://github.com/user-attachments/assets/5fa4458e-911f-4ce0-afee-dbc9a5da1f7c" />


---
## Three Video Chunking Strategies
- [source](https://github.com/databyjp/video-search-elastic-jina-demo)
- How you split a video determines what each chunk captures

1. **Fixed Length** -- **(Time-Based)**
   - **Split every N seconds**
   - How this works:
     - Simple and predictable chunks.
     - May cut mid-sentence or mid-thought.
   - Overall:
     - **Simplest to implement**
     - **Predictable chunk count**
    

2. **Transcript-Based** -- **(Semantic)**
   - **Split at topic boundaries**
   - How this works:
     - Uses video transcript to find natural breaks in speech and meaning.
  - Overall:
    - **Semantically coherent**
    - **Better search relevance**
4. **Visual (Scene-Based)**
  - **Split at visual changes**
  - How this works:
    - **Detects shot changes, slide transitions, or scene cuts in the video.**
  - Overall:
    - **Visually coherent chunks**
    - **Great for visual search**
---
## Three Layers of Video
- All videos actually have 3 distinct searchable information streams:

1. **Visual -- What's actually on the screen**
   - images
   - graphics
   - people
   - text overlays
   - scene composition
   - visual context

2. **Speech -- The spoken words**
   - Transcript/narration -- the semantic meaning of what someone says

3. **Audio -- Non-speech sound**
   - Music
   - sound effects
   - ambient noise --> information beyond just words



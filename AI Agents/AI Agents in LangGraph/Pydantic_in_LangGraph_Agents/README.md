# Pydantic in LangGraph Agents


---
# Why use Pydantic with LangGraph?

1. **Data Validation & Parsing**
   - Defines how data should be structured using standard Python type checks, automatically enforcing these rules.
   - LLM gives output in unstructured data --> Pydantic validates these outputs

2. **Type Hint Integration**
   - Python type annotations are used to define schemas.
   - This reduces the need for verbose validation code.

3. **Fast Performance**
   - Core validation engine written in RUST -- VERY FAST!

4. **Strict and Lax Modes**
   - Supports BOTH strict mode (enforcing strict types) AND lax mode (attempting to coerce data -- converting "1" to 1)

5. **Clear Error Handling**
   - Provides detailed errors when data validation fails.
  
6. **JSON Schema Generation**
   - Pydantic models can easily generate JSON schemas for documentation or validation in other languages.

---
# Jev

## What is Jev?
- **Non-Generative Design:** 
   - Unlike GPT or Claude, Jev produces no text. 
   - You supply context, questions, and predefined options, and it instantly returns typed decisions with confidence scores.

- **Speed and Efficiency:** 
   - By using a single forward pass instead of sequential token generation, it acts like a high-intelligence programmatic switch statement (routing, tagging, or filtering) with lower cost and latency than traditional LLMs.

- **Zero-Shot Operation:** 
   - It requires no upfront training data or fine-tuning, allowing you to define new classification categories at runtime.

## What is Jev used for?
- Jev acts as a fast classification layer for tasks like intent routing, sentiment scoring, and yes/no evaluation, returning structured, confidence-scored answers instead of generated text, and doing it with a single API call rather than a custom-trained model per task.

## Is Jev more accurate than a trained BERT classifier?
- Not usually. In benchmark testing, a small trained encoder with a logistic regression head beat Jev on three of four datasets (Banking77, emotion, phishing), sometimes by a wide margin, because it had access to task-specific labeled training data that Jev didn’t use.

## Is it Different from GLiClass or Other Zero-Shot Models?

- Functionally, Jev operates in the same conceptual design space as existing zero-shot classification models like GLiClass or encoder-based architectures. 
- However, there are key distinctions in packaging, training, and accessibility:

   - **Proprietary Packaging vs. Open Architectures:** 
      - Models like GLiClass and open-weights alternatives (such as Laya) provide transparent or open-weights approaches to general-purpose zero-shot text classification. 
      - Jev packages this capability into a closed, hosted commercial API backed by specialized training like Reinforcement Learning for Calibrated Decisions (RLCD)

   - **Inference and Usability:** 
      - Jev is heavily optimized as an out-of-the-box cloud API (available via routing gateways like OpenRouter or Vercel) that delivers consistent, high-tier intelligence-matching probability scores without needing local encoder/decoder infrastructure management

   - **Core Innovation:** 
      - Many engineers view Jev less as a brand-new machine learning breakthrough and more as an exceptionally polished commercial product and marketing wrapper around advanced zero-shot classification and calibration concepts that open-source communities have explored for years.


## When does Jev outperform trained classifiers?
- Jev pulls ahead when there’s no labeled training data available, when categories or routing rules change dynamically without a chance to retrain, or when a task requires answering many questions about the same input in one batched call.

## Why is Jev faster than typical LLM calls?
- Jev doesn’t generate text token by token. 
- It appears to use a single forward pass to extract output logits or allowed tokens directly, similar in spirit to how BERT-style encoders classify text in one pass, rather than the sequential, auto-regressive generation typical LLMs use.

## Does Jev need any training data to work?
- No. Jev operates zero-shot, meaning you define categories or questions at runtime without labeled examples. 
- This is its main advantage over both fine-tuned BERT classifiers and frozen-embedding logistic regression models, both of which require labeled data upfront.
---
# Open-Source Alternatives to Jev
- Jev is closed source. 
- TypeSafe has not released open weights or training code and has not announced plans to. 
- For teams that need to run classification inside their own network, or that do not want a waitlist between them and production, the open ecosystem moved fast. It helps to split the options into two groups: established zero-shot classifiers that predate Jev, and new projects that copy Jev's interface.

1. **GliClass** -- based on GliNER architecture
2. **NLI-based zero-shot models** -- includes models such as DeBERTa-v3 checkpoints fine-tuned on entailment datasets, remain a solid baseline starting point.
3. **CAPPr (completion after prompt probability)**
   - Uses any open causal LLM, but instead of letting the model generate, it scores the probability of each candidate completion. 
   - This turns a generative model into a classifier with a fixed output set.

---
# Jev Resources/References
- [Fast Classification Models, LLMs, and the Apache Iceberg Lakehouse](https://dev.to/alexmercedcoder/fast-classification-models-llms-and-the-apache-iceberg-lakehouse-387d)
- [Jev vs Classifiers, Embeddings and Zero-Shot Models](https://jevaiguide.com/compare/jev-vs-classifiers/)
- [Jev vs BERT and Zero-Shot NLI: What the Benchmarks Actually Show](https://www.mindstudio.ai/blog/jev-vs-classic-classifiers-benchmark)
- [Pydantic AI Adds Jev to Cut Classification Latency 6x Without Generating Tokens](https://alphasignal.ai/news/pydantic-ai-adds-jev-to-cut-classification-latency-6x-without-generating-tokens)
- [What Is Jev AI? A Practical Guide to System One and Executable Decisions](https://huggingface.co/blog/sora-2/what-is-jev-ai-a-practical-guide-to-system-one-and)
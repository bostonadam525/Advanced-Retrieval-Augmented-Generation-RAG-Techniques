# RAG Architectures for Unstructured Documents
* A repo devoted to system architecture, design, and implementation of various aspects of RAG pipelines for working with unstructured documents and data sources.





# ETL Pipelines for RAG
* There are various ETL pipeline architectures for RAG systems. We will go into some of them here.

## 3 Pipeline (FTI) Architecture
* This system helps you split the dev process into 3 components:
1. **Feature Pipeline**
   * Transforms incoming data into features & labels.
   * These are stored and versioned in a feature store.
   * The feature store is the central repository of your data features.
   * This means features can be accessed and shared only through the feature store.
2. **Training Pipeline**
   * Ingestion of a specific version of the features & labels from the feature store.
   * This outputs the trained LLM model weights, which are stored and versioned inside a model registry.
   * The LLM models will be accessed and shared only through the model registry.
3. **Inference Pipeline**
   * Uses a given version of the features from the feature store.
   * Downloads a specific version of the model from the model registry.
   * The final goal is to output the predictions to a client.

* FTI Architecture is below - [source](https://medium.com/decodingml/an-end-to-end-framework-for-production-ready-llm-systems-by-building-your-llm-twin-2cc6bb01141f)

![image](https://github.com/user-attachments/assets/097458a0-e285-4823-b0b9-8630f87b0d49)







# Standard RAG





# Scalability for RAG Systems







# References
1. [End-to-end framework for production-ready LLM systems](https://medium.com/decodingml/an-end-to-end-framework-for-production-ready-llm-systems-by-building-your-llm-twin-2cc6bb01141f)

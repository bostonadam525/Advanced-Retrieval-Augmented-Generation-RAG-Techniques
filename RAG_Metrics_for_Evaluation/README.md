# RAG Metrics for Evaluation - Overview, Resources, and Experiments
* By Adam Lang


# Classes of RAG LLM Evaluation Metrics
1. Qualitative & Ethical Metrics
   * Assess things such as tone, toxicity, and bias in the generative outputs.
   * These metrics help determine if the LLM’s output contains harmful, offensive, or inappropriate content.
    
2. Use-case metrics
   * Domain-specific measures that assess how effectively an LLM application accomplishes its intended real-world objectives.
   * These could include AI policy adherence, which ensures that the output aligns with AI regulations for a particular region, or impact metrics.
     
3. Hallucinaton metrics
   * These are one of the most important metrics as these measure the "correctness" and "factuality" of an LLM response.

* Diagram showing above classes of metrics:

![image](https://github.com/user-attachments/assets/21e6f5b0-5977-4ca5-aa88-430439d53299)


* Another view of the classes of evaluation metrics: [source](https://dagshub.com/blog/llm-evaluation-metrics/)

![image](https://github.com/user-attachments/assets/3319ba00-b09f-4c2a-a2aa-e52e45e689fb)



# Testing LLM Outputs
* These are a general list of testing frameworks that can be used to automate and manually test LLM outputs.
1. BERTScore
   * Pros of using BERTScore
     * Uses BERT based models and contextual embeddings.
     * Cosine Similarity to evalute semantic similarity of outputs.
     * Token matching for:
       * Precision
       * Recall
       * F1 score
     * Importance weighting
     * Baseline rescaling
  * Cons of BERTScore
     * Metrics can be biased depending on data
     * BERTScore doesn’t consider syntactic structures
     * Doesn’t do well with idiomatic expressions, slang, or culture refs
  * Resources for BERTScore
      * [Simple Examples](https://medium.com/@abonia/bertscore-explained-in-5-minutes-0b98553bfb71)
      * [Issues with BERTScore](https://medium.com/@lukasheller1989/watch-out-with-leveraging-bertscore-for-the-evaluation-of-language-models-ed28dc365435)
2. BLEU Score
   * Pros of using BLEU Score
      * n-gram matching
      * standard benchmarks for NLP
      * Quick evaluations
      * Provides a baseline
   * Cons of using BLEU Score
      * Does not use embeddings.
      * Historical benchmark method. 
   * Resources for BLEU Score
     * [BLEU Score vs. BERTScore](https://medium.com/@shraddhasri9648/bertscore-vs-bleu-score-for-evaluating-machine-generated-text-87b962f56f84#:~:text=While%20BERTScore%20provides%20a%20more,of%20machine%2Dgenerated%20text%20quality.)
3. RAGAS
   * Pros of using RAGAS
     * Open source
     * Simple to use
     * Available in: 
       * AWS Bedrock
       * Python
     * Multiple metrics available for:
       * Retrieval
       * Generation
   * Cons of using RAGAS
       * Need a test set with ground truths.
   * Resources for RAGAS
       * [Evaluating RAG sytems using RAGAS](https://ai.plainenglish.io/evaluating-rag-systems-using-ragas-framework-d4b8df74d027)
       * [RAGAS in AWS Bedrock](https://docs.ragas.io/en/latest/howtos/customisations/aws-bedrock.html)
4. DeepEval
  * Pros of DeepEval
      * Open source
      * Unit testing for LLM outputs (similar to Pytest)
      * Multiple metrics
  * Cons of DeepEval
      * Unit testing LLM outputs can have its disadvantages depending on your system architecture, data, and use cases. 
  * Resources for DeepEval
      * [DeepEval github](https://github.com/confident-ai/deepeval)
      * [Unit testing with DeepEval](https://dev.to/shannonlal/unit-testing-llms-with-deepeval-4ljl)
      * [Example using DeepEval](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation#fine-tuning-metrics)
5. AWS Automated Evaluation
    * Pros of AWS eval
       * AWS metrics:
          * Accuracy 
          * Robustness
          * Toxicity
       * OOTB evaluation of LLM outputs in Bedrock
    * Cons of AWS eval
       * Metric calculations may differ based on the tasks you are trying to evaluate
            * text generation
            * text summarization
            * Q&A
            * text classification
    * Resources for AWS bedrock
         * [AWS bedrock LLM evals](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report-programmatic.html)

6. SentenceTransformers Distance Metrics
   * If you are usng SBERT embeddings, it is important to know and consider whether or not the distance metrics you are using apply to your data.
   * Cosine similarity is not always the metric to use as it only considers direction.
   * Dot Product is used when you need magnitude and direction. Same with Euclidean Distance.
   * Resource:
      * [SBERT Distance Metrics for evaluation](https://osanseviero.github.io/hackerllama/blog/posts/sentence_embeddings/#distance-between-embeddings)
    

# Resources
* [Evaluation Leaderboards and Frameworks](https://www.shedge.com/05-generative-ai/llm/tools/evaluation-tools/)
* [How to Evaluate LLM Summarization](https://towardsdatascience.com/how-to-evaluate-llm-summarization-18a040c3905d)
* [LLM Evaluation Essentials: From LLM-as-a-Judge to Perplexity (Part 1)](https://medium.com/data-analytics-at-nesta/llm-evaluation-essentials-from-llm-as-a-judge-to-perplexity-part-1-04294bfff304#:~:text=LLM%2Das%2Da%2Djudge%3A%20This%20technique%20is%20widely,own%20or%20other%20LLM%20outputs.)
* [LLM Evaluation Metrics: Benchmarks, Protocols & Best Practices](https://dagshub.com/blog/llm-evaluation-metrics/)
* [Perplexity for LLM Evaluation](https://www.comet.com/site/blog/perplexity-for-llm-evaluation/)

# RAG Metrics for Evaluation - Overview, Resources, and Experiments
* By Adam Lang

# RAG and NLG Metrics -- A Full Review
* This diagram comes from the paper [Leveraging Large Language Models for NLG Evaluation: Advances and Challenges](https://arxiv.org/abs/2401.07103)
* This is an important taxonomy to consider when choosing your metric(s) for evaluating RAG and any generative outputs. 

![image](https://github.com/user-attachments/assets/d48e6051-63c9-4028-8710-6ad05590e423)


# RAG Pipeline Evaluation 
* Below is a very general diagram of the 2 main components of RAG pipelines and their respective eval metrics:

![image](https://github.com/user-attachments/assets/e33e51da-ed32-4ca8-b5d1-3cdb36c06bdb)


## RAG Pipeline Components with metrics
* There are 2 main components of a basic RAG pipeline:

1. **Retriever**
  * Usually a knowledge base or vector embedding store (vector DB).
  * Metrics
    * **Context Precision**
      * Most relevant information is prioritized at top of retrieval.
      * Similar to precision machine learning metric.
      * The actual percentage of the results that are relevant to the original input or query.
    * **Context Recall**
      * All relevant chunks retrieved related to original query.
      * Similar to recall machine learning metric.
      * Recall is the percentage of total relevant results correctly classified by the LLM.
    * **Hit Rate**
      * A binary score indicating the presence of the correct chunk in the retrieved chunks.
    * **MRR (Mean Reciprocal Rank)**
      * A metric used to evaluate the effectiveness of search engines, recommendation systems, or any system that involves ranking a list of items.

2. **Generator**
    * LLM of choice
    * Metrics
      * **Faithfulness**
        * faithfulness represents the accuracy of explanations in illustrating the LLM’s actual reasoning, i.e., why and how the model reached a particular decision.
        * Paper reference: https://arxiv.org/html/2402.04614v2
      * **Relevancy**
        * Relevancy measures the quality of your RAG pipeline's generator by evaluating how relevant the actual_output of your LLM application is compared to the provided input.

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



# Testing LLM Outputs (Natural Language Generation)
* These are a general list of testing frameworks that can be used to automate and manually test LLM outputs.

## Model Based Metrics for Natural Language Generation Evaluation 
1. **BERTScore**
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

2. **BLEURT**
   * BLEURT is an evaluation metric for Natural Language Generation.
   * It takes a pair of sentences as input, a reference and a candidate, and it returns a score that indicates to what extent the candidate is fluent and conveys the meaning of the reference.
   * It is comparable to **sentence-BLEU**, **BERTscore**, and **COMET**.
   * [BLEURT Github](https://github.com/google-research/bleurt?tab=readme-ov-file)
  
3. **BARTScore**
   *  The BART score approaches the problem of evaluating a LLM generated text as a text generation problem.
   *  BART is a specifically trained sequence-to-sequence model or encoder-decoder model.
   *  BART is capable of calculating a score using the **weighted log probability** of one generated text y given another input text x.
   *  The BARTScore supports the evaluation of generated text from different perspectives (faithfulness, precision, recall, …) which makes it powerful a powerful metric to consider. 


4. **UniEval**
   * This framework was developed by Elastic Search Labs.
   * UniEval uses T5 another encoder-decoder model (similar to BART) as the base model it was trained on.
   * The pre-trained UniEval model is biased towards summarization, but the authors note that "RAG Question Answering can be viewed as an aggressive summarization task when avoiding parametric memory for accurate responses."
   * The most interesting aspect of the UniEval is that it has been trained across the following dimensions:
      * **Coherence** -- gauging the formation of a cohesive body from all sentences.
      * **Consistency** -- assessing the factual alignment between the answer and the context.
      * **Fluency** -- evaluating the quality of individual sentences.
      * **Relevance** -- measuring the factual alignment between the answer and the ground truth.
  * [UniEval Github](https://github.com/maszhongming/UniEval)
  * [Elastic Search Labs RAG Eval metrics including UniEval](https://www.elastic.co/search-labs/blog/evaluating-rag-metrics)

5. **COMET**
   * COMET (Crosslingual Optimized Metric for Evaluation of Translation) is a metric for automatic evaluation of machine translation that calculates the similarity between a machine translation output and a reference translation using token or sentence embeddings.
   * [COMET metric github](https://github.com/Unbabel/COMET)

## N-Gram Based Metrics
1. **BLEU Score**
   * Pros of using BLEU Score
      * **n-gram matching**
      * standard benchmarks for NLP
      * Quick evaluations
      * Provides a baseline
   * Cons of using BLEU Score
      * Does not use embeddings.
      * Historical benchmark method. 
   * Resources for BLEU Score
     * [BLEU Score vs. BERTScore](https://medium.com/@shraddhasri9648/bertscore-vs-bleu-score-for-evaluating-machine-generated-text-87b962f56f84#:~:text=While%20BERTScore%20provides%20a%20more,of%20machine%2Dgenerated%20text%20quality.)

2. **ROUGE Score**
   * ROUGE or "Recall-Oriented Understudy for Gisting Evaluation" is usually used to assess the effectiveness of machine-generated summaries.
   * ROUGE evaluates how similar a generated passage is to reference passages by **counting shared words or phrases**.
   * ROUGE differs from BLEU in its scoring, as it **calculates recall**, while **BLEU calculates precision**.
   * This means ROUGE primarily looks at determining **how much information from the reference passages is contained within the generated passage.**
     * This is what makes ROUGE a very common choice for **tasks related to summarization.**

3. **METEOR Score**
  * METEOR or "Metric for Evaluation of Translation with Explicit Ordering" is a metric widely used in the field of machine generation.
  * METEOR differs from the n-gram metrics above by incorporating the **harmonic mean of precision and recall.**
  * In addition, METEOR works on a word-level at **synonyms, stemming and word order (via fragmentation penalty)** when assessing word matching/n-gram matching.
  * The word level complexity is what makes METEOR succesful in achieiving a stronger correlation with human judgments as compared to BLEU.

## Intrinsic Metrics for NLG Evaluation
1. **Perplexity**
   * Perplexity (also known as PPL) is perhaps one of the most common metrics for assessing Language Models (LLMs).
   * To calcualte perplexity you need to have access to the probability distribution for each word generated by your language model.
   * This is a measure of how confidently the model is able to predict a sequence of words or tokens.
      * The higher the perplexity, the less confidently the model predicts the observed sequence.
   * [Read more about Perplexity here](https://www.comet.com/site/blog/perplexity-for-llm-evaluation/)
  
2. **Accuracy**
3. **Precision**
4. **Recall**
5. **F1 Score**

## Frameworks for NLG Evaluation 
1. **RAGAS**
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
2. **DeepEval**
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

3. **Comet Opik**
   * Open source eval framework.
   * [Comet Opik github](https://github.com/comet-ml/opik)
  
4. **deepchecks**
   * [deepchecks](https://www.deepchecks.com/)

5. **Langfuse**
   * Open source LLM observability framework.
   * [Langfuse github](https://github.com/langfuse/langfuse)

6. **LangSmith**
   * LangChain's framework for LLM observability.
   * [LangSmith link](https://www.langchain.com/langsmith)

7. **promptfoo**
   * open source framework for LLM observability.
   * [Link to promptfoo](https://www.promptfoo.dev/)
  
  
8. **AWS Automated Evaluation**
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
     
    * [AWS Refchecker](https://github.com/amazon-science/RefChecker)

9. **SentenceTransformers Distance Metrics**
   * If you are usng SBERT embeddings, it is important to know and consider whether or not the distance metrics you are using apply to your data.
   * Cosine similarity is not always the metric to use as it only considers direction.
   * Dot Product is used when you need magnitude and direction. Same with Euclidean Distance.
   * Resource:
      * [SBERT Distance Metrics for evaluation](https://osanseviero.github.io/hackerllama/blog/posts/sentence_embeddings/#distance-between-embeddings)

10. **NLG-metricverse**
   * NLG Metricverse is an end-to-end Python library for NLG evaluation, devised to provide a living unified codebase for fast application, analysis, comparison, visualization, and prototyping of automatic metrics.
   * [NLG-metricverse github](https://github.com/disi-unibo-nlp/nlg-metricverse)
  

11. **Machine Translate.org**
   * This isn't a RAG specific framework but a good resource for translation and NLG metrics.
   * [Machine Translation Metrics](https://machinetranslate.org/metrics)



# Resources
* [Awesome LLM for NLG Evaluation Papers](https://github.com/chongyangtao/LLMs-for-NLG-Evaluation)
* [Evaluation Leaderboards and Frameworks](https://www.shedge.com/05-generative-ai/llm/tools/evaluation-tools/)
* [Fine-Tuning vs Retrieval-Augmented Generation (RAG)](https://medium.com/@heyamit10/fine-tuning-vs-retrieval-augmented-generation-rag-36175d49f4e3)
* [How to Evaluate LLM Summarization](https://towardsdatascience.com/how-to-evaluate-llm-summarization-18a040c3905d)
* [LLM Evaluation Essentials: From LLM-as-a-Judge to Perplexity (Part 1)](https://medium.com/data-analytics-at-nesta/llm-evaluation-essentials-from-llm-as-a-judge-to-perplexity-part-1-04294bfff304#:~:text=LLM%2Das%2Da%2Djudge%3A%20This%20technique%20is%20widely,own%20or%20other%20LLM%20outputs.)
* [LLM Evaluation Metrics: Benchmarks, Protocols & Best Practices](https://dagshub.com/blog/llm-evaluation-metrics/)
* [LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation)
* [Perplexity for LLM Evaluation](https://www.comet.com/site/blog/perplexity-for-llm-evaluation/)

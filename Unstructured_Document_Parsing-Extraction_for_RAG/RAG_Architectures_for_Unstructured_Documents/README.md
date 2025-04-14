# RAG Architectures for Unstructured Documents
* A repo devoted to system architecture, design, and implementation of various aspects of RAG pipelines for working with unstructured documents and data sources.


## Full end-to-end RAG Pipeline with unstructured data
* This is an excellent example of an end-to-end pipeline with unstructred data sources (e.g. websites).
* [Source](https://medium.com/decodingml/i-replaced-1000-lines-of-polling-code-with-50-lines-of-cdc-magic-4d31abd3bc3b)
* The specific details of each compontent of this pipeline implementation are in the sections below.

![image](https://github.com/user-attachments/assets/9d35a0bd-0a9e-4c75-912f-4cf41fcf31a5)




# ETL Pipelines for RAG
* There are various ETL pipeline architectures for RAG systems. We will go into some of them here.

## 3 Pipeline (FTI) Architecture
* This system helps you split the dev process into 3 components.

---
### 1. **Feature Pipeline**
   * Transforms incoming data into **features & labels.**
   * These are stored and versioned in a **feature store.**
   * The feature store is the **central repository** of your data features.
   * This means features can be accessed and shared only through the feature store.

#### 1.1 Feature ETL Pipelines
* You can setup 1 ETL pipeline vs. many individual pipelines for each data source.

##### 1.2 Feature Data Types
1. HTML Website data
   * This data could be extracted multiple ways but if you are "scraping" websites this is generally how you might do this:
     a. Use a web based scraping library such as Python's selenium to crawl the website(s).
     b. Use a Python library such as BeatifulSoup to parse and extract the HTML content.
     c. Data cleaning & normalization of the extracted HTML
     d. Save the normalized but still VERY RAW data to a NoSQL database such as MongoDB.

2. HTM documents
3. PDF documents

##### 1.31 Feature ETL Database Selection
* The database selected can vary based on your data types and needs.
* MongoDB is a standard NoSQL document database that has a vector DB version called "Mongo DB Atlas" so this may be a top choice for storing website text and text from PDF documents.
* However, if you are scraping MULTIMODAL data from websites and other unstructured documents you may want to consider using a different database or databases all together.
  * This approach can vary depending upon how you are going to create features from your data.
  * You may want to have:
    1. NoSQL database
    2. SQL database
    3. Graph database
    4. Data Lakes
    5. ...etc...
* **A key point to remember at this stage of the pipeline is that this is a database to store RAW data BEFORE you create your features, vectors and embeddings. This database is NOT expected to be a vector database as that component comes into the pipeline AFTER feature extraction/selection in the Feature Pipeline. This database is essentially a staging area for raw data.**

##### 1.32 Feature ETL Data Storage
* There are various data storage techniques and data models for unstructured data.
* The **Object Document Mapping (ODM)** is a well known technique that maps between an object model in an application and a document database.
  * Abstracting database interactions through model classes allows the ODM to simplify the process of storing and managing data in a document-oriented database such as MongoDB.
  * **The Role of Metadata**
      * Metadata plays a crucial role in object-document mapping by defining how objects and their attributes are translated into documents and fields. 
      * Metadata can be stored as key-value pairs, annotations, or other structured formats. 
      * Examples of metadata include:
        1. Mapping object properties to document fields. 
        2. Defining the data type of a field. 
        3. Specifying relationships between objects and their documents. 
        4. Enabling indexing for faster data retrieval. 

* **How is Metadata used in Object-Document Mapping?**
  1. **Mapping Objects to Documents**
    * Metadata is used to define how the properties of an object are mapped to fields within a document.
    * For example an Employee object with id, name, and salary properties can be mapped to a document with corresponding fields.
  2. **Specifying Relationships**
    * Metadata can be used to define relationships between different objects and their documents.
    * For example, if an Employee object has a reference to a Department object, metadata can define how this relationship is represented in the documents.
  3. **Customizing Mapping Behavior**
    * Metadata can be used to customize the mapping behavior, such as defining custom converters for data types or using custom strategies for handling relationships.

    
##### 1.4 Data Pipeline CDC 
* It is important with any Feature pipeline to have a mechanism setup to communicate updates and changes in your data to the feature pipeline.
* **"CDC" or "Change Data Capture" Patterns is the most common mechanism used for this.**
  * [see this link](https://superlinked.com/vectorhub/building-blocks/data-sources/data-modality#kAGPz?utm_source=community&utm_medium=blog&utm_campaign=oscourse)
  * A key requirement of data retrieval systems is ensuring the underlying representations (i.e. vector embeddings) accurately reflect the **most up to date source data.**
  * **As underlying data changes – (e.g., product updates, user activities, sensor readings) corresponding vector representations must also be kept current.**
  * There are various approaches to CDC such as [source](https://www.qlik.com/us/change-data-capture/cdc-change-data-capture#:~:text=Change%20data%20capture%20(CDC)%20refers,a%20downstream%20process%20or%20system.)
    **1. Batch recomputation**
        * Periodically rebuilding all vectors from scratch as the new data piles up.
        * But batch recomputation ignores incremental changes between batches

    **2. Log-based CDC**
        * **This is the most efficient way to implement CDC.**
        * When a new transaction comes into a database, it gets logged into a log file with no impact on the source system. 
        * And you can pick up those changes and then move those changes from the log.

    ![image](https://github.com/user-attachments/assets/e987e056-f348-4737-bc12-7eb5a91750d1)

    **3. Query-based CDC**
        * Simply put, you query the data in the source to find changes.
        * This approach is more invasive to the source systems because you need something like a timestamp in the data itself.

   **4. Trigger-based CDC**
        * Changing the source application to trigger the write to a change table and then move it.
        * This reduces database performance because it requires multiple writes each time a row is updated, inserted, or deleted.

* **Where does CDC fit into the overall pipeline?**
  * CDC's primary purpose is to identify and capture changes made to database data, such as insertions, updates, and deletions.
  * CDC then logs these events and sends them to a message queue (e.g. RabbitMQ).
  * This allows other pipeline components to react to the data changes in real time by reading from the queue, ensuring that all application parts are up-to-date.
  * This is a great breakdown of where CDC fits into the overall pipeline as an "orchestrator". [source](https://medium.com/decodingml/i-replaced-1000-lines-of-polling-code-with-50-lines-of-cdc-magic-4d31abd3bc3b)
 

![image](https://github.com/user-attachments/assets/3d781d0b-25af-4ea1-9355-2ac0c2ec5613)


* **Why do we even need the CDC pattern?**
1. **Real-time Data Synchronization**
   * CDC facilitates near-real-time data integration and syncing.

2. **Highly Efficient Data Pipelines**
   * Allows incremental data loading, which is more efficient than bulk load operations.

3. **Minimized System Impact**
   * CDC minimizes the impact on the source system by reducing the need for performance-intensive queries.

4. **Event-Driven Architectures**
   * Enables event-driven architectures by streaming database events.


##### 1.5 Feature Streaming Ingestion Pipeline
* This can vary depending upon your data and use case(s).
* If you are streaming your data ingestion then you would build a separate pipeline called a **streaming ingestion pipeline**.
* Key points about adding a streaming component:
  1. This is separate from the data pipeline.
  2. Communcation with Data pipeline is separate
 

##### 1.6 Scope of Feature Pipeline
1. Ingestion part of RAG system.
2. Transformation of Raw source data:
  * Cleaning
  * Splitting --> Tokenization --> Chunking
  * Vector Embedding creation
  * Inserting and indexing embeddings in a vector DB
  * Usually individual data types are processed independently 
    * Even if all of your data is text-based, you may need to chunk and embed them using completely different strategies as "one size does not fit all."
    * You may have multimodal data in PDF files (e.g. Tables, Text, Images), HTM data, and the list goes on.

3. Data Storage
* The training pipeline will ONLY have access to the feature store, which is where you will store the vector embeddings, in a vector database of choice (e.g. Qdrant, Weaviate, Pinecone, ChromaDB, etc..)
  * This can also be a SQL or NoSQL database that has vector capabilities such as MongoDB Atlas which is NoSQL, or a SQL DB that uses the pgvector add on. 
* Data will be stored in the Vector Database in 2 collections:
  * 1. The cleaned data (without using vectors as indexes — store them in a NoSQL fashion).
  * 2. The cleaned, chunked, and embedded data (leveraging the vector indexes of Qdrant)

* The training pipeline needs access to the data in **both formats** as we want to fine-tune an LLM on standard and augmented prompts.
  * With the cleaned data, we will create the prompts and answers.
  * With the chunked data, we will augment the prompts (aka RAG).

##### 1.7 Streaming pipelines vs. batch pipelines?
* [source for comparing streaming vs. batch](https://medium.com/@remisharoon/batch-vs-streaming-data-pipeline-making-the-right-choice-c08b4d080580)
* There various reasons why you may want to implement either of these formats such as:
  1. A streaming pipeline with a CDC pattern is the **most efficient way to sync two databases between each other.**
     * This means syncing the "raw data" that is stored in a MongoDB NoSQL database to the Vector Database.
     * **Otherwise, you will have to implement batch polling or pushing techniques that are not easily scalable when working with big data.**
     * Using CDC + a streaming pipelines allows you to process ONLY the changes to the source database with the raw data (e.g. MongoDB NoSQL database) without any overhead cost or computational overload.

  2. Using a streamling pipeline allows your source and vector DBs to remain in sync with each other
     * This gives your Feature Pipeline and the rest of the system to always have access to **current data** for RAG.

###### 1.8 Challenges of Streaming Pipelines
* Streaming pipelines provide real-time data processing and can deliver instantaneous insights, they often come with their own set of challenges such as:

  1. Infrastructure Complexity
     * Building a real-time system often requires specialized tools and technologies that can be complex to set up and maintain.

  2. Cost
     * Real-time processing might demand more computational power and thus can be more expensive than batch processing.

  3. Error Handling
     * When processing data in real-time, there’s limited opportunity to rectify errors, which might lead to inaccurate insights.

  4. State Management
     * Maintaining and managing state in a real-time system can be challenging, especially when dealing with large volumes of data.

  5. Data Ordering
     * Ensuring that data is processed in the order it’s received can be tricky in a distributed streaming system.

  6. Integration Challenges
     * Not all systems and tools integrate seamlessly with real-time data platforms.

###### 1.9 Advantages of Streaming Pipelines
* While batch processing has its perks, there are various scenarios where real-time processing is essential:

  1. Immediate Decision Making
     * If your business operations require making split-second decisions, real-time insights are crucial.
     * For example, fraud detection in banking.

  2. Dynamic Pricing
     * Businesses like ride-sharing services or e-commerce platforms might use real-time data to adjust prices based on current demand.

  3. Monitoring and Alerts
     * Real-time systems are crucial for monitoring applications and sending out immediate alerts, such as health monitoring systems or network security applications.

  4. Interactive Applications in Production
     * If users need data in real-time such as an LLM-RAG based application or real-time analytics and insights. 

###### 1.10 Advantages of Batch processing 
  1. Simplicity
     * Batch systems are generally simpler to design, implement, and maintain.
  2. Scalability
     * Much easier to scale batch processes horizontally. You can process massive volumes of data by merely adding more machines to your cluster.
  3. Cost-Effective
     * With the ability to schedule jobs during off-peak times, batch processing can be more cost-effective.

  4. Mature Tools
     * Many mature tools and platforms are available for batch processing, which are well-documented and widely adopted.

  5. Error Rectification
     * In batch processing, there’s a window of opportunity to correct errors before data is further processed or analyzed.


---
### 2. **Training Pipeline**
   * Ingestion of a specific version of the **features & labels** from the feature store.
   * This outputs the trained LLM model weights, which are stored and versioned inside a model registry.
   * The LLM models will be accessed and shared only through the model registry.


---
### 3. **Inference Pipeline**
   * Uses a given version of the features from the feature store.
   * Downloads a specific version of the model from the model registry.
   * The final goal is to output the predictions to a client.

* **FTI Architecture is below** - [source](https://medium.com/decodingml/an-end-to-end-framework-for-production-ready-llm-systems-by-building-your-llm-twin-2cc6bb01141f)

![image](https://github.com/user-attachments/assets/097458a0-e285-4823-b0b9-8630f87b0d49)

#### Why is the 3 Pipeline Architecture so great?
1. More intuitive design
2. Brings structure on a higher level, all Machine Learning systems can be reduced to these 3 components
3. Defines **transparent interface** between the 3 components
   * MUCH easier for cross-functional collaboration
   * ML system has been built with modularity in mind at Stage 0
4. The 3 components can be divided up between multiple teams (if necessary)
5. The 3 components can use the most focused best stack of technologies available for each specific job in the pipeline rather than focusing on 1 infrastructure ONLY.
6. Each separate component can be deployed, scaled, and monitored independently OFFLINE and ONLINE.
7. Feature pipeline can be scaled as either:
   * Batch
   * Streaming
   * Batch and Streaming

#### Origin of the 3 pipeline design
* This came from Jim Dowlings 2023 paper from Hopworks you can find [here](https://www.hopsworks.ai/post/mlops-to-ml-systems-with-fti-pipelines)
* One of the novel points of Jim's paper is that he points out that having a separate feature engineering pipeline opens the door to using the **right tools for the right data**.
  * As you can see in the diagram from his original paper below, based on the type of data you have it tells us what feature extraction tools to build into the feature pipeline.
    1. Size of Data (e.g. small vs. BIG)
    2. Data frequency (e.g. Batch processing vs. Real-Time)
    3. Data types (e.g. text, image, audio, multi-modal, etc.)

![image](https://github.com/user-attachments/assets/59ff6306-1bdd-4b6b-b620-37b185dd1f15)

---
# Classic RAG
* **Goal: Semantic Search and Retrieval.**
* This is an example of a very basic Standard RAG Architecture from NVIDIA.
* Some of the components we see below:
1. **Llama-Index**
   * API orchestrator for the entire system which acts as the system router.
2. Enterprise Data
   * this can be any multimodal data in a raw data store such as a NoSQL or SQL or Graph DB or in a general knowledge base on AWS.
3. `E5-large`
   * this is the embedding model from NVIDIA.
   * It has been optimized for scalability with `TensorRT`.
4. Milvus
   * this is a vector database where the vectorized data has been stored.
5. Llama-2-Triton
   * this is the LLM being used in the RAG system.
   * The LLM has been optimized using the Triton inference server. 
6. DGX Cloud
   * this is NVIDIA's native AI based cloud platform where the entire system is deployed.

![image](https://github.com/user-attachments/assets/07cce779-d480-410e-97a2-060ca1d944c2)


## Clasical RAG - Ingest & Query Architecture
* The classical data ingestion and query architecture from NVIDIA is below:

![image](https://github.com/user-attachments/assets/cc036f06-cdee-486d-826c-952d441f8fda)


### 1. Classical ETL-Ingestion Pipeline
* Image courtesy of NVIDIA

1. Data retrieval
2. Data pre-processing
   * Cleaning & Wrangling
   * Splitting & Chunking
   * Duplicates removal
3. Data tokenization

![image](https://github.com/user-attachments/assets/ccde4521-7606-41e3-a356-b3ada44ea428)


### 2. Embedding Generation
* Image courtesy of NVIDIA

![image](https://github.com/user-attachments/assets/0a09aa15-4b6a-4440-aa2f-96117961a9b6)


### 3. Indexing
* Image courtesy of NVIDIA
* The goal is to create indices so that when the data is inserted into a vector database the retrieval process is more efficient.
* There has been studies done on this that show that the order in which your vectors were indexed and the ultimate order of insertion into a vector database can significantly influence the retrieval results based on the specific retrieval algorithm that you are using in your vector DB (e.g. HNSW).
* This is must read [blog post](https://www.marqo.ai/blog/understanding-recall-in-hnsw-search) that came from the arxiv paper written by Marqo vector DB. It explains the importance of the insertion order of your vectors and the embedding models used can significantly influence the recall of your system. 

![image](https://github.com/user-attachments/assets/47c7fe0b-636d-4bad-8f49-3fcb71d3c861)


### 4. Vector Database(s)
* Various search algorithms depending upon the vector database vendor.


### 5. Prompts
* Prompt templates are a pre-define abstraction often used through APIs such as LangChain or Llama-Index.


### 6. RAG Frameworks
* LangChain vs. Llama-Index is often the debate.
  * Both frameworks have their advantages and disadvantages.
  * LangChain is easier and more intuitive "out of the box".
  * Image below courtesy of NVIDIA.

https://www.marqo.ai/blog/understanding-recall-in-hnsw-search



* Alternatives
  * Haystack
  * Flowise
 

### 7. Embedding Models
* MTEB benchmarks
* BEIR benchmarks
* Embedding Types
  1. Dense Embeddings (e.g. SentenceTransformers)
  2. Sparse Embeddings (e.g. SPLADE)
  3. Multilingual
  4. Rerankers (Cross-Encoders)
  5. Static Word Embeddings (e.g. Word2Vec, GLoVe)
  6. Image embeddings
  7. Graph embeddings

### 8. LLMs
* Choose your LLM based on your use case(s), data, compute power and scalability (among other things).


---
# Agent Driven RAG
* **Goal: Agent with tool calling functions is added to the RAG pipeline.**
* This is an example of agent driven RAG from NVIDIA.
* Common Types of Agentic RAG:
1. "Zero-Shot"
   * This is similar to classic RAG where a "zero shot" query or prompt is sent to the LLM with retrieval.
   * If the answer is NOT in the vector store, the agent uses the tools it has access to in order to go find the answer.

2. "Chain of Thought RAG" - CoT
   * This is more closely related to the ReAct framework or "reason and act".
   * This means that the agent is instructed to "reason and act" to find the correct answer to a query given a series of steps with guidance. 

![image](https://github.com/user-attachments/assets/c8d419c9-2d3c-4678-9b4e-037f044212b3)




---
# Guardrails RAG
* **Goal: Guardrails are applied to the pipeline to limit certain answers to queries.**
* The example below is from NVIDIA using the NVIDIA nemo guardails.
* There are 3 types of general guardrails that NEMO offers:
1. Topical guardrails
   * Prevents specific topics of choice from being answered by the RAG application.

2. Safety guardrails
   * Prevent unwanted language and responses (e.g. biases, toxicity).
  
3. Security guardrails
   * Prevents access to unwanted 3rd party applications and only allows certain APIs or external applications access.


![image](https://github.com/user-attachments/assets/a05ee982-5d08-4f0a-a7a7-9c35f0299cd0)

---
# Scalability for RAG Systems







# References
1. [End-to-end framework for production-ready LLM systems](https://medium.com/decodingml/an-end-to-end-framework-for-production-ready-llm-systems-by-building-your-llm-twin-2cc6bb01141f)

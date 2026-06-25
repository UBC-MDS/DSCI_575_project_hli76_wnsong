# Final Discussion

## Step 1: Improve Our Workflow

### Data Scaling
- Number of products used: 94,319
- Our chosen dataset has already scaled up and implemented in Milesonte1 as shown in the milestone1_exploration.ipynb EDA demonstration. There is no change to sampling strategy. 

### LLM Experiment
- Models compared
    - Name: "llama-versatile-70b", Family: Llama 3.3, Size: 70B
    - Name: "gpt-oss-20b", Family: GPT OSS, Size: 20B

- Results and discussions
    - Prompt used 1: "quiet fast-boiling kettle for small apartment that keeps water warm"
        - **Outputs 1 ("llama-versatile-70b")**: "Based on the provided context, I recommend the DADDY COOL Mini Fridge Cooler & Warmer (ASIN: B07ZPM3QGT) is not a kettle, however, for a quiet fast-boiling kettle, the Gevi Milk Frothing Pitcher (ASIN: B08KGB9563) review mentions an electric kettle that boils water quickly and has a quiet operation, but it is actually a milk frothing pitcher. A more suitable option can be found in the review for the SimpleReal - Pour Over Coffee Kettle with Thermometer (ASIN: B07NL7LLBK), it doesn't explicitly state that it's fast-boiling, but it does have a thermometer and keeps water warm for pour-over coffee. Another option is the Danby DKT17C2SSDB 1.7L Kettle (ASIN: B01GV52L4U), it doesn't have explicit reviews about being quiet or keeping water warm, but it is a stainless steel kettle. It's also worth noting that none of these products perfectly match the requested features, but they are the closest matches based on the provided context."
        - **Outputs 1 ("gpt-oss-20b")**: "I don’t know."

    - Prompt used 2: "high-power blender for nut butter and ice under $200"
        - **Output 2 ("llama-versatile-70b")**: "I don't know."
        - **Output 2 ("gpt-oss-20b")**: "I don't know."

    - Prompt used 3: "countertop oven that fits a 9x13 pan and has air fry mode"
        - **Output 3 ("llama-versatile-70b")**: "The provided context does not mention a countertop oven that fits a 9x13 pan and has an air fry mode. However, it does mention that a customer got rid of their convection toaster oven and countertop air fryer after purchasing the Frigidaire Gallery GCRG3060AF 5 Cu.Ft. Stainless Free-Standing Gas Range with Air Fry (ASIN: B0853F5RVG). This suggests that the range's air fry feature was sufficient to replace their countertop air fryer. Additionally, the GASLAND Chef Professional Electric Wall Oven 5.0 Cu.Ft. Convection (ASIN: B09QMBBGNF) review mentions that the oven can produce excellent air fry results when set to "convection roast" mode, but it is not a countertop oven. Unfortunately, based on the provided context, I don't know of a specific countertop oven model that fits a 9x13 pan and has an air fry mode."
        - **Output 3 ("gpt-oss-20b")**: "I don't know."

    - Prompt used 4: "lightweight cordless vacuum for hardwood, pet hair, and stairs under 5 kg"
        - **Output 4 ("llama-versatile-70b")**: "The acum Cordless Stick Vacuum (ASIN: B009A6OTU2) is a lightweight option that weighs less than 5 kg and is suitable for hardwood floors, pet hair, and stairs. It has a 6-in-1 handheld cleaner design and a 30-minute lasting runtime, making it ideal for cleaning various surfaces. With its powerful 23KPa suction, it can effectively pick up pet hair and other debris."
        - **Output 4 ("gpt-oss-20b")**: "The only cordless vacuum listed in the context that is described as lightweight and suitable for hardwood floors, pet hair, and stairs is the acum Cordless Stick Vacuum (ASIN B009A6OTU2). It’s marketed as a “lightweight & 30‑minute lasting runtime” 6‑in‑1 handheld cleaner that works well on hardwood, carpet, mattress, and pet‑hair‑heavy areas. The review summary notes it’s “ideal for hardwood floor carpet mattress & pet hair cleaning,” which covers the surfaces you mentioned. Weight: The product description in the context does not give an exact weight figure, so we cannot confirm that it is under 5 kg. However, it is marketed as lightweight, so it is a strong candidate if you need a vacuum that’s easy to carry up stairs."

    - Prompt used 5: "convection toaster oven for baking small batches"
        - **Output 5 ("llama-versatile-70b")**: "For baking small batches, you may want to consider the Air Fryer Toaster Oven 13.5 Quart Large Air Fryer Oven 10in1 Convection Oven Airfryer with Rotisserie, Dehydrator & Pizza,Smart Oven-Black (ASIN: B095YNXNDW). It has a 5.0 average rating and reviewers have mentioned that it is easy to use and has a setting for specific foods, such as chicken wings. One reviewer mentioned that it is easy to make fried sweet potato using the "French fry" one-click selection. Additionally, another reviewer used it to cook chicken wings and achieved juicy and tender results. However, if you're looking for a more specific convection toaster oven, you might want to consider the GE JS750EFES 30" Slate Electric Slide-In Smoothtop Range - Convection (ASIN: B00NN11ZT8), but it might be larger than what you need for small batches. It's also worth noting that some reviewers have mentioned using liners or mats, such as the Premium Liners for Ninja Foodi Air Fryer Bottom of toaster Oven Mat (ASIN: B0C6FSYD83), to make cleaning easier."
        - **Output 5 ("gpt-oss-20b")**: "Convection toaster oven for small‑batch baking. The Air Fryer Toaster Oven 13.5 Quart (ASIN B095YNXNDW) is a 10‑in‑1 convection oven that’s well suited for baking small batches. Reviewers praise its “easy to use” design and “convection” function, which makes it ideal for quick, even baking of items such as cookies, cupcakes, or small batches of pizza. It also offers additional features (rotisserie, dehydrator, air‑frying) without sacrificing the core convection baking capability."

    - Key observations: From testing the 5 queries, "llama-versatile-70b" models had 1 output saying "I don't know" and generally had more detailed answers to queries. On the other hand, "gpt-oss-20b" had 2 outputs saying "I don't know" and with relatively shorter answers to quries.

- Which model we chose and why: We choose to stay with "llama-versatile-70b" model as it provides better answer overall from previous query tests.


## Step 2: Additional Feature
### What We Implemented
- Description of the feature: 
    - We scaled up over 94k products, which is way more than the assigned 10k criteria. 
    - We also tried to add tool agumentation feature through using Tavily. However, after multiple tests on Langchain libraries, we found new Langchain package wasn't stable and had issue importing the required package. We tried to switch to langchain-classic package but it contains depreciation issue and conflicts in communication with Groq service. Given the time constraint, we gave up the implementation in order to keep our current app working. (Notes: The try out records could be found under the "final_milestone" branch on the Github repository. This branch's app.py can also successfully run locally, but LLM queries might fail due to the Langchain and Groq imcompatibility issue as mentioned and triggers error messages by Groq.)
- Key results or examples: From using over 94k products and over 2 million rows of product reviews, this scale offers better capabilities by providing richer answers to users' queries.


## Step 3: Improve Documentation and Code Quality

### File Structure:
- We have double checked that required files are existing and in the correct location.

### Documentation Update
- Summary of `README` improvements: We add clear instruction and description in README for users to follow more easily.

### Code Quality Changes
- Summary of cleanups: We removed legacy commented out code blocks to make the scripts easier to read. All functions have Docstrings prepared.


## Step 4: Cloud Deployment Plan

The following plan outlines the architecture for deploying our **Smart Amazon Product Query Assistant** to a cloud platform, specifically focusing on Amazon Web Services (AWS) as the primary provider.

### 1. Data Storage

Transitioning from local file storage to a cloud-native architecture requires decoupling the storage from the application logic to allow for scalability.

* **Raw Data:** The original Amazon JSONL and Parquet files will be stored in an **Amazon S3** bucket (e.g., Standard tier). S3 provides highly durable, cheap object storage perfect for raw, immutable datasets.
* **Processed Data:** The cleaned, merged, and aggregated Parquet files (e.g., `Appliances_products.parquet`) will also reside in **Amazon S3**. DuckDB is highly optimized for cloud workloads and can query Parquet files directly from S3 using the `httpfs` extension, meaning we do not need to load the entire dataset into a traditional relational database.
* **Vector Index (Semantic):** Storing a local `faiss.index` file does not scale well across multiple concurrent server instances. We will migrate the vector embeddings to a managed Vector Database, such as **Pinecone**, **Milvus**, or **AWS OpenSearch Serverless**. This allows the app to query the index via API without holding the entire matrix in memory.
* **BM25 Index:** Similarly, loading a `bm25.pkl` file into memory limits horizontal scaling. We will migrate the lexical search to **AWS OpenSearch** (which uses Elasticsearch under the hood). OpenSearch natively handles distributed BM25 scoring and can also double as our vector database for a unified retrieval backend.

### 2. Compute

* **App Hosting:** The application will run on **AWS EC2** instances. Deploying the Streamlit frontend, potentially decoupled with a FastAPI backend served via Uvicorn, provides a highly customizable environment. Alternatively, we can containerize the app using Docker and deploy it to **AWS ECS (Elastic Container Service) with Fargate** for a fully serverless container setup that abstracts away the underlying EC2 maintenance.
* **Handling Concurrency:** To handle multiple users, the application will be placed behind an **AWS Application Load Balancer (ALB)**. The ALB will distribute incoming traffic across multiple EC2 instances or ECS tasks. We will utilize Streamlit's `@st.cache_resource` to ensure that any necessary in-memory models (like the SentenceTransformer encoding model) are only loaded once per instance, reducing memory overhead per user session.
* **LLM Inference:** We will continue using an **API-based approach** (e.g., Groq or OpenAI). Hosting a 70B parameter model like LLaMA-3.3 locally on an AWS EC2 GPU instance (like a `p4d` or `g5` instance) is extremely cost-prohibitive for a baseline deployment. API routing allows us to leverage massive compute power with minimal latency while only paying for the tokens we generate. 

### 3. Streaming/Updates

* **Incorporating New Products:** To handle incoming product data without downtime, we will implement a micro-batching architecture. New Amazon products and reviews will drop into an "Ingestion" S3 bucket. An **AWS Lambda** function will be triggered upon file creation to process the text, generate the new `all-MiniLM-L6-v2` embeddings, and upsert the new vectors and metadata directly into our live OpenSearch/Vector DB. 
* **Pipeline Up-to-Date:** For larger, scheduled pipeline updates (e.g., recalculating the global BM25 IDF weights or rebuilding DuckDB aggregations), we will use an orchestration tool like **Apache Airflow** or **AWS Step Functions**. A daily or weekly cron job will spin up an AWS Glue or EC2 worker to run the ETL scripts, seamlessly hot-swapping the new data into the production S3 buckets and databases without interrupting the user experience.
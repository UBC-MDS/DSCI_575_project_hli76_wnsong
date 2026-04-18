# Smart Amazon Product Query Assistant

## Motivation
We are creating a context-aware product search assistant that returns relevant Amazon products based on natural language queries. The assistant contains multiple systems and will be implemented in two Milestone stages:

#### Milestone 1:
- BM25
- Semantic Search
- Hybrid Search (Combination of BM25 and Semantic)

#### Milestone 2:
- LLM (To be implement...)

## Installation

### Clone the project and install the Python environment
```bash
# Clone the repository
git clone https://github.com/UBC-MDS/DSCI_575_project_hli76_wnsong.git
cd DSCI_575_project_hli76_wnsong

# Create and activate the conda environment
conda env create -f environment.yml
conda activate dsci575-project
```

### Download Data
Run the following command will download and generate the required files:
```bash
python src/download_data.py
```
- raw data for reviews and meta data as parquet file
    - `data/raw/Appliances_meta_raw.parquet`
    - `data/raw/Appliances_reviews_raw.parquet`
- merged data (reviews + meta data) where each review is a single row in a parquet file
    - `data/processed/Appliances_merged.parquet`
- document ids (`parent_asin`) in a pickle file
    - `data/processed/Appliances_doc_ids.pkl`
- product documents in a pickle file
    - `data/processed/Appliances_product_documents.pkl`
- merged product data where each product is a single row in a parquet file
    - `data/processed/Appliances_products.parquet`

### Other Saved Files
- `data/queries.csv`: 21 queries used for testing
- Files created by `src/bm25.py`:
    - `data/processed/bm25.pkl` 
    - `data/processed/tokenized_corpus.pkl` 
- Files created by `src/semantic.py`:
    - `data/processed/faiss.index`
- feedback from `app/app.py`
    - `data/processed/feedback.csv`

### Run Web Application Locally
Run the following command at the project root:
```bash
streamlit run app/app.py
```

Streamlit will display a local URL such as :
```bash
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:[port]
  Network URL: http://[address]
  External URL: http://[address]
```
Please check your terminal for the correct address.

### Project Structure
```
│
├── app/
│   └── app.py                                 # Streamlit UI for querying BM25, Semantic, and Hybrid search
│
├── data/
│   ├── processed/                             # Preprocessed, indexed, and model-ready data
│   │   ├── Appliances_merged.parquet          # Product-level merged metadata + aggregated reviews
│   │   ├── Appliances_product_documents.pkl   # Text documents used for BM25 & Semantic search
│   │   ├── Appliances_doc_ids.pkl             # Mapping from document index → parent_asin
│   │   ├── Appliances_products.parquet        # Product-level structured data (title, price, features)
│   │   ├── bm25.pkl                           # Saved BM25 index
│   │   ├── tokenized_corpus.pkl               # Tokenized corpus used by BM25
│   │   └── faiss.index                        # FAISS vector index for Semantic search
│   │
│   ├── raw/
│   │   ├── Appliances_meta_raw.parquet        # Original metadata from Amazon Reviews 2023
│   │   └── Appliances_reviews_raw.parquet     # Original review data from Amazon Reviews 2023
│   │
│   └── queries.csv                            # Query set used for evaluation and testing
│
├── notebooks/
│   ├── milestone1_exploration.ipynb           # Exploration of BM25, Semantic, Hybrid methods
│   ├── demo.ipynb                             # Demonstration notebook for search pipeline
│   └── <OTHER NOTEBOOKS>                      # Additional analysis or experimentation
│
├── src/
│   ├── bm25.py                                # BM25 implementation + index building
│   ├── semantic.py                            # Semantic search using SentenceTransformer + FAISS
│   ├── retrieval_metrics.py                   # Precision@k, Recall@k, MRR, and evaluation utilities
│   ├── utils.py                               # Helper functions (loading data, preprocessing, etc.)
│   └── download_data.py                       # Script to download and preprocess Amazon data
│
├── results/
│   └── milestone1_discussion.md               # Evaluation results and discussion for Milestone 1
│
├── README.md
├── environment.yml
├── .env                                       # Optional: API keys for LLM-based querying (not in repo)
└── LICENSE
```

## Tool Augmentation
This project utilizes a LangChain Agent setup to augment the standard RAG pipeline with external tool calling capabilities. 

**Web Search Tool (`TavilyClient`)**
- **Description:** A custom LangChain tool wrapped around the Tavily API. 
- **Logic:** When the user queries information outside the scope of the historical dataset (e.g., "What is the current price of ASIN B001234?" or "Is there a newer model?"), the Llama 3 model routes the request through the `web_search` tool. The agent automatically executes the query, extracts the text snippets from the live web, and synthesizes them with the local vector search context to provide a complete answer.

## Data Source

There are total 33 product categories in the Amazon Reviews 2023 dataset. Each category contains two files:
- Review file (`<Category>.jsonl.gz`): user-written reviews, ratings, timestamps, votes.
- Metadata file (`meta_<Category>.jsonl.gz`): product titles, descriptions, features, price, categories.

- For script-based download, please see Installation section above.

- For manual download and field descriptions: 
- Project website:[https://amazon-reviews-2023.github.io/](https://amazon-reviews-2023.github.io/)

- Hugging Face dataset: [https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023)

## License

See [LICENSE](LICENSE) for details.

## Team

See [team.txt](team.txt) for team member information.
# Smart Amazon Product Query Assistant

## Motivation
We are creating a context-aware product search assistant that returns relevant Amazon products based on natural language queries. We are creating multiple systems serving the search in two Milestone stages:

Milestone 1:
- BM25
- Semantic
- Hybrid (Combination of BM25 and Semantic)

Milestone 2:
- LLM (To be implement...)

## Installation

### Clone the project and install Python environment
```bash
# Clone the repository
git clone https://github.com/UBC-MDS/DSCI_575_project_hli76_wnsong.git
cd DSCI_575_project_hli76_wnsong

# Create and activate the conda environment
conda env create -f environment.yml
conda activate dsci575-project
```

### Download Data
Run the command will obtain the following files:
```bash
python src/download_data.py
```
- raw data for reviews and meta data as parquet file
- merged data (reviews + meta data) where each review is a single row in a parquet file
- document ids (`parent_asin`) in a pickle file
- product documents in a pickle file
- merged product data where each product is a single row in a parquet file

### Other Saved Files
- `data/queries.csv`: 21 queries used for testing
- files created by `src/bm25.py`:
    - `data/processed/bm25.pkl` 
    - `data/processed/tokenized_corpus.pkl` 
- files created by `src/semantic.py`:
    - `data/processed/faiss.index`

### Run Web Application Locally
Run the following code in the terminal at project root to run the app
```bash
streamlit run app/app.py
```

Depending on your machine, Streamlit would provide local url for easier access, for example:
```bash
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:[streamlit_provided_address]
  Network URL: http://[streamlit_provided_address]
  External URL: http://[streamlit_provided_address]
```
Please read through your terminal to get the address

### Project Structure
```
│
├── app/
│   └── app.py
├── data/
│   ├── processed/                             # cleaned/ chunked / indexed files
│   │   ├── Appliances_merged.parquet
│   │   ├── Appliances_product_documents.pkl
│   │   ├── Appliances_doc_ids.pkl
│   │   ├── Appliances_products.parquet
│   │   ├── bm25.pkl
│   │   ├── tokenized_corpus.pkl
│   │   └── faiss.index
│   ├── raw/
│   │   ├── Appliances_meta_raw.parquet
│   │   └── Appliances_reviews_raw.parquet
│   └── queries.csv
│
├── notebooks/
│   ├── milestone1_exploration.ipynb
│   ├── demo.ipynb
│   └── <OTHER NOTEBOOKS>
│
├── src/
│   ├── bm25.py
│   ├── semantic.py
│   ├── retrieval_metrics.py
│   ├── utils.py
│   └── download_data.py
│
│── results/
│   └── milestone1_discussion.md
│
│
├── README.md
├── environment.yml
├── .env                 # Optional: API keys for Query with Chat (not in repo)
└──
```

## Data Source

There are total 33 product categories. Each category has two files:
- Review file (`<Category>.jsonl.gz`): user-written reviews, ratings, timestamps, votes.
- Metadata file (`meta_<Category>.jsonl.gz`): product titles, descriptions, features, price, categories.

- For script download, please see Installation instruction above.

- For self download instructions and field descriptions are at [https://amazon-reviews-2023.github.io/](https://amazon-reviews-2023.github.io/).

- Hugging Face: [https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023)

## License

See [LICENSE](LICENSE) for details.

## Team

See [team.txt](team.txt) for team member information.
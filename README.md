# DSCI_575_project_hli76_wnsong

Smart Amazon Product Query Assistant
- a context-aware product search assistant that returns relevant Amazon products based on natural language queries

### Data

Data sources:
- Dataset Website: [https://amazon-reviews-2023.github.io/](https://amazon-reviews-2023.github.io/)
- Hugging Face: [https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023)

There are total 33 product categories. Each category has two files:
- Review file (`<Category>.jsonl.gz`): user-written reviews, ratings, timestamps, votes.
- Metadata file (`meta_<Category>.jsonl.gz`): product titles, descriptions, features, price, categories.

Download instructions and field descriptions are at [https://amazon-reviews-2023.github.io/](https://amazon-reviews-2023.github.io/).

### install Python environment

```bash
conda install -f environment.yml
```

### Project Structure
```
DSCI_575_project_hli76_wnsong/
│
├── README.md
├── environment.yml
├── .env
│
├── data/
│   ├── raw/
│   │   ├── Appliances_meta_raw.parquet
│   │   └── Appliances_reviews_raw.parquet
│   └── processed/             # cleaned/ chunked / indexed files
│       ├── Appliances_merged.parquet
│       ├── Appliances_product_documents.pkl
│       └── Appliances_doc_ids.pkl
│
├── notebooks/
│   ├── milestone1_exploration.ipynb
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
├── app/
│   └── app.py
```

### Download Data
Run the following code will obtain the following files:
- raw data for reviews and meta data as parquet file
- merged data (reviews + meta data) for each product in a single parquet file
- document ids (`parent_asin`) in a pickle file
- product documents in a pickle file

```bash
python src/download_data.py
```

### Run Web Application Locally
Run the following code in the terminal at project root to run the app
```bash
streamlit run app/app.py
```
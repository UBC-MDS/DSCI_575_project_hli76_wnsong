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
│   ├── raw/                   # downloaded .jsonl.gz files (put them in .gitignore)
│   └── processed/             # cleaned/ chunked / indexed files
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
│   └── <OTHER_SCRIPTS>
│
│── results/
│   └── milestone1_discussion.md
│
├── app/
│   └── <YOUR_APP>.py           # single app, updated each milestone
```

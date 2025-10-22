Title: SHAP-BASED_FS_SMOTE

Short description
This project applies SHAP-based feature selection and class rebalancing with SMOTE to improve intrusion detection performance. The workflow covers data preprocessing, MASV-XGB score calculation, feature selection, and detection/classification.

Data source

Network Intrusion Dataset (Kaggle): https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset
Project structure

data/: data folder (kept even if empty via .gitkeep)
code/: source code (optionally includes main.py for end-to-end execution)
notebooks/:
Preprocessing.ipynb
Calculating_XGBMASV.ipynb
FS_SMOTE_Detection.ipynb
requirements.txt
README.md
Requirements

Python 3.8+ (3.10/3.11 recommended)
pip
Optional: Jupyter Notebook/Lab
Environment setup

Create and activate a virtual environment:
Windows:
python -m venv venv
venv\Scripts\activate
macOS/Linux:
python -m venv venv
source venv/bin/activate
Install dependencies:
pip install --upgrade pip
pip install -r requirements.txt
Prepare the data

Download the dataset from Kaggle: https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset
Place your files under data/, for example:
data/train.csv
data/test.csv
If you don’t have data yet, the data/ folder is kept in Git via data/.gitkeep.
How to run
Option A: via Jupyter Notebook

jupyter notebook (or jupyter lab)
Open notebooks/Preprocessing.ipynb and run all cells
Open notebooks/Calculating_XGBMASV.ipynb and run all cells
Open notebooks/FS_SMOTE_Detection.ipynb and run all cells
Option B: via integrated script

If code/main.py is set up for an end-to-end pipeline:
python code/main.py
Common arguments (adjust if available):
--input data/train.csv
--output outputs/
--config configs/config.yaml
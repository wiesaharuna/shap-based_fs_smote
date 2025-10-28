Title: SHAP-BASED_FS_SMOTE

Short description:

This project applies SHAP-based feature selection and class rebalancing with SMOTE to improve intrusion detection performance. The workflow covers data preprocessing, MASV-XGB score calculation, feature selection, and detection/classification.


Data source:

Network Intrusion Dataset (Kaggle): https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset


Project structure:

data/: data folder (kept even if empty via .gitkeep)

code/: source code (optionally includes main.py for end-to-end execution)


notebooks/:

Preprocessing.ipynb

Calculating_XGBMASV.ipynb

FS_SMOTE_Detection.ipynb


Requirements: 

Python 3.8+ (3.9.13 recommended)

pip

numpy = 1.26.4

pandas = 2.1.4

scikit-learn = 1.2.2

xgboost = 2.0.3

imbalanced-learn = 0.11.0

shap = 0.46.0

openpyxl = 3.0.10

jupyter = 1.1.1

nbconvert = 7.16.4

nbclient = 0.10.0

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


Place your files under data/, for example, "cicids2017_sampled_50_.csv"

Due to the size issue, we haven’t uploaded the data yet; therefore, the data folder is kept in Git via data/.gitkeep.


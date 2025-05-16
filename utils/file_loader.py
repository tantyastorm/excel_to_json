import os
import pandas as pd

def load_excel_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if not file_path.endswith(('.xlsx', '.xls')):
        raise ValueError("Only .xlsx or .xls files are supported")
    return pd.read_excel(file_path, engine="openpyxl")

import os
import pandas as pd

def load_excel_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if not file_path.lower().endswith(".xlsx"):
        raise ValueError("Only .xlsx files are supported")
    try:
        return pd.read_excel(file_path, engine="openpyxl")
    except Exception as exc:
        raise ValueError(f"Could not read workbook: {exc}") from exc

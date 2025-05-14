import pandas as pd

def load_excel(file_path: str):
    """Load the Excel file and return a pandas DataFrame."""
    df = pd.read_excel(file_path, engine='openpyxl')
    # Strip any leading/trailing whitespace from the column names
    df.columns = df.columns.str.strip()
    return df

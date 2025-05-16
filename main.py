import argparse
from utils.file_loader import load_excel_file
from processor.header_parser import get_headers
from processor.json_exporter import export_json

def main():
    parser = argparse.ArgumentParser(description="Smart Excel to JSON Exporter")
    parser.add_argument('--file', required=True, help="Path to Excel file (.xlsx)")
    parser.add_argument('--orientation', required=True, choices=["row", "column"], help="Is the data organized by row or column?")
    args = parser.parse_args()

    df = load_excel_file(args.file)
    headers = get_headers(df, args.orientation)
    
    if args.orientation == "row":
        extracted = df[headers].to_dict(orient="records")
    else:
        extracted = df.T[headers].to_dict()
    
    export_json(extracted)

if __name__ == "__main__":
    main()

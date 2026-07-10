import argparse
import sys
from utils.file_loader import load_excel_file
from processor.header_parser import get_headers
from processor.json_exporter import export_json

def main():
    parser = argparse.ArgumentParser(description="Smart Excel to JSON Exporter")
    parser.add_argument('--file', required=True, help="Path to Excel file (.xlsx)")
    parser.add_argument('--output', default="output.json", help="Path for the exported JSON file")
    args = parser.parse_args()

    try:
        df = load_excel_file(args.file)
        headers = get_headers(df)
        extracted = df[headers].to_dict(orient="records")
        export_json(extracted, args.output)
    except (FileNotFoundError, ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

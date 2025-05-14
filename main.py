import argparse
from utils.file_loader import load_excel
from processor.header_parser import parse_headers
from processor.json_exporter import export_to_json

def main():
    parser = argparse.ArgumentParser(description='Process an Excel file with book data and export it to JSON.')
    parser.add_argument('input_file', help='The Excel file to process')
    parser.add_argument('output_file', help='The output JSON file')
    args = parser.parse_args()

    # Load the Excel file
    df = load_excel(args.input_file)

    # Parse the Excel rows and convert to structured data
    books_data = parse_headers(df)

    # Export the structured data to JSON
    export_to_json(books_data, args.output_file)

if __name__ == '__main__':
    main()

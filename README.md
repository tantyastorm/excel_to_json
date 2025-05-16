# Smart Excel to JSON Exporter

A lightweight, flexible CLI tool that processes messy Excel files and exports clean JSON based on user-selected headers and data orientation.

## Features
- Accepts `.xlsx`/`.xls` files
- Supports row- or column-based data orientation
- Custom header selection by user
- Clean JSON export
- Modular structure with unit tests
- CLI support (via argparse)

## Usage

```bash
python main.py --file sample_data/test.xlsx --orientation row

## Project Structure
''
smart_excel_exporter/
├── main.py
├── config.py
├── requirements.txt
├── utils/
│   ├── file_loader.py
│   └── logger.py
├── processor/
│   ├── header_parser.py
│   └── json_exporter.py
├── tests/
│   ├── test_file_loader.py
│   ├── test_header_parser.py
│   └── test_json_exporter.py
├── sample_data/
│   └── test.xlsx
''

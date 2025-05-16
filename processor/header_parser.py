def get_headers(df, orientation):
    print(f"Detected columns: {df.columns.tolist() if orientation == 'row' else df.index.tolist()}")
    headers_input = input("Enter the headers to extract (comma-separated): ")
    headers = [h.strip() for h in headers_input.split(',')]
    return headers

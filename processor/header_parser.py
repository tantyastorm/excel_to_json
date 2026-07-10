def parse_headers(headers_input):
    headers = []
    seen = set()
    for header in headers_input.split(","):
        clean_header = header.strip()
        if not clean_header or clean_header in seen:
            continue
        headers.append(clean_header)
        seen.add(clean_header)
    if not headers:
        raise ValueError("Select at least one field to export")
    return headers


def validate_headers(headers, available_headers):
    invalid_headers = [header for header in headers if header not in available_headers]
    if invalid_headers:
        available = ", ".join(str(header) for header in available_headers)
        invalid = ", ".join(str(header) for header in invalid_headers)
        raise ValueError(f"Invalid field(s): {invalid}. Available fields: {available}")


def get_headers(df):
    print(f"Available headers: {df.columns.tolist()}")
    headers_input = input("Enter the headers to extract (comma-separated): ")
    headers = parse_headers(headers_input)
    validate_headers(headers, df.columns.tolist())
    return headers

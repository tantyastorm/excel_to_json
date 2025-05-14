def parse_headers(df):
    """Parse each row as a book's data."""
    books_data = []
    
    for index, row in df.iterrows():
        book_info = {
            "Title": row["title"],
            "Price": row["price"],
            "Stock": row["stock"],
            "Image URL": row["image_url"]
        }
        
        # Handle special subcolumns like 'Hide' and 'Color'
        for col in df.columns:
            if 'Hide' in col or 'Color' in col:
                base_name = col.split()[0]
                if base_name not in book_info:
                    book_info[base_name] = {"Hide": None, "Color": None}
                if 'Hide' in col:
                    book_info[base_name]["Hide"] = row[col]
                elif 'Color' in col:
                    book_info[base_name]["Color"] = row[col]

        books_data.append(book_info)
    
    return books_data

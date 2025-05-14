from utils.file_loader import load_excel
from processor.header_parser import parse_headers

def test_parse_headers():
    # Load a test file with book data
    df = load_excel('sample_data/test_books.xlsx')
    
    # Parse the data
    books_data = parse_headers(df)
    
    # Basic assertions
    assert isinstance(books_data, list)
    assert len(books_data) > 0  # Should have at least one book
    assert "Title" in books_data[0]
    assert "Price" in books_data[0]
    assert "Stock" in books_data[0]
    assert "Image URL" in books_data[0]

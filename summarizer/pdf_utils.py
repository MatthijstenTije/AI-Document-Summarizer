import fitz

def convert_pdf_to_text(path):
    """
    Extracts text from a PDF file using fitz.
    """
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

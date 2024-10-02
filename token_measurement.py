import os
import tiktoken
from PyPDF2 import PdfReader

# Define the tokenize function
def tokenize(text: str) -> list[int]:
    encoding = tiktoken.encoding_for_model('gpt-4-turbo')
    return encoding.encode(text)

# Path to your output directory
output_dir = 'files/output'  # Replace with the actual path to your output directory

# List to store filenames and their token counts
file_token_counts = []

# Iterate over each file in the output directory
for filename in os.listdir(output_dir):
    if filename.endswith('.txt'):  # Adjust the file extension if needed
        file_path = os.path.join(output_dir, filename)
        # Use PyPDF2 to read the PDF file
        try:
            reader = PdfReader(file_path)
            content = ''
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    content += text
                else:
                    print(f"Warning: No text found on page {page_num + 1} of {filename}")
            token_count = len(tokenize(content))
            file_token_counts.append((filename, token_count))
        except Exception as e:
            print(f"Error reading {filename}: {e}")

# Print out the token counts for each file
for filename, token_count in file_token_counts:
    print(f"{filename}: {token_count} tokens")


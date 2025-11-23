from PyPDF2 import PdfReader, PdfWriter

# List of PDF files to read from
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

# Pages to extract from each PDF (0-based index)
# Example: from file1 take pages 0 and 2, from file2 take page 1, etc.
pages_to_extract = {
    "file1.pdf": [0, 2],
    "file2.pdf": [1],
    "file3.pdf": [0, 3]
}

# Create PDF writer object
writer = PdfWriter()

# Loop through PDFs and add selected pages
for pdf in pdf_files:
    reader = PdfReader(pdf)
    for page_num in pages_to_extract[pdf]:
        if page_num < len(reader.pages):     # avoid errors if page doesn't exist
            writer.add_page(reader.pages[page_num])

# Save to a new PDF
output_file = "merged_selected_pages.pdf"
with open(output_file, "wb") as f:
    writer.write(f)

print("Merged PDF created successfully:", output_file)

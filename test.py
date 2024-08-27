import os
import pandas as pd
from PyPDF2 import PdfReader
from pathlib import Path

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ''
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to convert text to Excel
def convert_to_excel(text_data, excel_file):
    # Split text into lines
    lines = text_data.split('\n')

    # Create a DataFrame
    df = pd.DataFrame(lines, columns=['Text'])

    # Write DataFrame to Excel
    df.to_excel(excel_file, index=False)
    print(f'Converted PDF to Excel: {excel_file}')

# Function to read from Excel
def read_excel_file(excel_file):
    df = pd.read_excel(excel_file)
    print('Contents of Excel file:')
    print(df)

# Main function
def main():
    pdf_file = '/home/sweety/Downloads/BANvsZIM-1ccmnyf4fot5h--2-598131234247246218951.pdf'   # Update with your PDF file path
    excel_file = '/home/sweety/output.xlsx'  # Output Excel file path

    # Check if PDF file exists
    if not os.path.exists(pdf_file):
        print(f'Error: PDF file not found at {pdf_file}')
        return

    # Extract text from PDF
    try:
        text_data = extract_text_from_pdf(pdf_file)
    except Exception as e:
        print(f'Error extracting text from PDF: {e}')
        return

    # Convert text to Excel
    convert_to_excel(text_data, excel_file)

    # Read from Excel
    read_excel_file(excel_file)

if __name__ == '__main__':
    main()

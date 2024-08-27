import PyPDF2
import pandas as pd

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ''
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
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

# Main function
def main():
    pdf_file = '/home/sweety/Downloads/BANvsZIM-1ccmnyf4fot5h--2-598131234247246218951.pdf'   # Update with your PDF file path
    excel_file = 'outdone.xlsx'                       # Output Excel file path

    # Extract text from PDF
    text_data = extract_text_from_pdf(pdf_file)

    # Convert text to Excel
    convert_to_excel(text_data, excel_file)

if __name__ == '__main__':
    main()

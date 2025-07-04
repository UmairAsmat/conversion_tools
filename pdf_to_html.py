import os
from pathlib import Path
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
import io

PDF_DIR = 'pdf_files'
HTML_DIR = 'htmls_files'

# Ensure output directory exists
os.makedirs(HTML_DIR, exist_ok=True)

def convert_pdf_to_html(pdf_path, html_path):
    try:
        with open(pdf_path, 'rb') as pdf_file, open(html_path, 'w', encoding='utf-8') as html_file:
            output = io.StringIO()
            laparams = LAParams()
            extract_text_to_fp(pdf_file, output, laparams=laparams, output_type='html', codec=None)
            html_file.write(output.getvalue())
        print(f"Converted: {pdf_path} -> {html_path}")
    except Exception as e:
        print(f"Failed to convert {pdf_path}: {e}")

def main():
    pdf_dir = Path(PDF_DIR)
    html_dir = Path(HTML_DIR)
    pdf_files = list(pdf_dir.glob('*.pdf'))
    if not pdf_files:
        print(f"No PDF files found in {PDF_DIR}")
        return
    for pdf_file in pdf_files:
        html_file = html_dir / (pdf_file.stem + '.html')
        convert_pdf_to_html(pdf_file, html_file)

if __name__ == '__main__':
    main()

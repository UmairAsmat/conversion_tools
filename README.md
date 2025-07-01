# html_to_text_converter

This project provides a Python script to convert HTML files in the `htmls_files` directory into plain text files in the `text_files` directory. It automates the process by opening each HTML file in your default web browser, selecting all content, copying it to the clipboard, and saving it as a `.txt` file.

## Features
- Batch convert HTML files to text
- Uses browser rendering for accurate text extraction
- Simple and easy to use

## Requirements
- Python 3.x
- [pyautogui](https://pypi.org/project/pyautogui/)
- [pyperclip](https://pypi.org/project/pyperclip/)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
1. Place your HTML files in the `htmls_files` directory.
2. Close other browser windows/tabs for best results.
3. Run the script:
   ```bash
   python html_to_text.py
   ```
4. The converted text files will appear in the `text_files` directory.

**Note:**
- The script will take control of your mouse and keyboard. Do not use your computer while it runs.
- Make sure your clipboard is working and your browser is set as the default for HTML files.

## Repository
[GitHub Repository](https://github.com/UmairAsmat/html_to_text_converter.git) 
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
This script converts all HTML files in the 'htmls_files' directory to text files in the 'text_files' directory by:
1. Opening each HTML file in the default web browser.
2. Simulating CTRL+A and CTRL+C to copy all content.
3. Reading the clipboard content.
4. Saving it as a .txt file in 'text_files'.

Requirements:
- pip install pyautogui pyperclip
- Close other browser windows/tabs for best results.
- Do not use your computer while the script runs (it will take over keyboard/mouse).
"""

HTML_DIR = os.path.join(os.path.dirname(__file__), 'htmls_files')
TEXT_DIR = os.path.join(os.path.dirname(__file__), 'text_files')

if not os.path.exists(TEXT_DIR):
    os.makedirs(TEXT_DIR)

html_files = [f for f in os.listdir(HTML_DIR) if f.lower().endswith('.html') or f.lower().endswith('.htm')]

# Set up headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

for html_file in html_files:
    html_path = os.path.abspath(os.path.join(HTML_DIR, html_file))
    file_url = f'file:///{html_path}'
    print(f"Processing: {html_file}")
    driver.get(file_url)

    # Get the visible text of the page
    body = driver.find_element("tag name", "body")
    text = body.text

    # Save to text file
    txt_file = os.path.splitext(html_file)[0] + '.txt'
    txt_path = os.path.join(TEXT_DIR, txt_file)
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Saved: {txt_file}\n")

driver.quit()
print("All files processed.")

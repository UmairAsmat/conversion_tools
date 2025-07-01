import os
import time
import webbrowser
import pyautogui
import pyperclip

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

for html_file in html_files:
    html_path = os.path.abspath(os.path.join(HTML_DIR, html_file))
    print(f"Processing: {html_file}")
    webbrowser.open(f'file:///{html_path}')
    time.sleep(3)  # Wait for browser to open and load

    # Select all and copy
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # Get clipboard content
    text = pyperclip.paste()

    # Save to text file
    txt_file = os.path.splitext(html_file)[0] + '.txt'
    txt_path = os.path.join(TEXT_DIR, txt_file)
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Saved: {txt_file}\n")
    time.sleep(1)  # Optional: wait before next file

print("All files processed.")

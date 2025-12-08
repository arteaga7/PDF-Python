#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:           read_pdf_pdfplumber.py
Author:         Antonio Arteaga
Last Updated:   2025-11-13
Version:        1.0
Description:
Text is obtained from a PDF file by using the pdfplumber library.
The PDF file should contain flat text only (pictures are ignored).
All text is saved in "output_txt".
Dependencies:   pdfplumber==0.11.8
"""

import pdfplumber

# PDF path
pdf_path = "./data/raw/text_and_img.pdf"
output_txt = "./pdfplumber_text.txt"

# Open the PDF file
with pdfplumber.open(pdf_path) as pdf:
    all_text = ""
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            print(f"\n--- Página {i + 1} ---\n")
            print(text[:40])                       # Show first 400 charaters
            all_text += text + "\n"
        else:
            print(
                f"⚠️ Page {i + 1} contains no selectable text (probably an image).")

# Save the text in a file
with open(output_txt, "w", encoding="utf-8") as f:
    f.write(all_text)

print(f"\n✅ Text saved in {output_txt}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:           pymupdf_fitz_example.py
Author:         Antonio Arteaga
Last Updated:   2025-11-18
Version:        1.0
Description:
Text is obtained from a PDF file by using the pymupdf (fitz) library.
The PDF file should contain flat text only (pictures are ignored).
This library is not recommended for scanned PDFs.
All text is saved in 'output_path'.
Dependencies:   fitz==0.0.1.dev2, PyMuPDF==1.26.6
"""
import fitz         # PyMuPDF

# Open the PDF
pdf_path = "./data/raw/vectorized_word_to_pdf.pdf"
output_path = "./fitz_text.txt"

# Open the PDF file
with fitz.open(pdf_path) as pdf:
    all_text = ""
    for i, page in enumerate(pdf, start=1):
        text = page.get_text()
        if text:
            print(f"\n--- Page {i + 1} ---\n")
            print(text[:40])                       # Show first 40 charaters
            all_text += text + "\n"
        else:
            print(
                f"⚠️ Page {i + 1} contains no selectable text (probably an image).")

# Save the text in a file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(all_text)

print(f"\n✅ Text is saved in {output_path}")

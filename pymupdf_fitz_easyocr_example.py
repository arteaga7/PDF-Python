#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:           pymupdf_fitz_easyocr_example.py
Author:         Antonio Arteaga
Last Updated:   2025-11-19
Version:        1.0
Description:
Text is obtained from a PDF file by using the pymupdf (fitz) and easyocr libraries.
The PDF file can contain flat text and pictures. All text is saved in "output_txt".
Dependencies:   fitz==0.0.1.dev2, PyMuPDF==1.26.6, easyocr==1.7.2
"""

import fitz                 # PyMuPDF
import easyocr

pdf_path = "./data/raw/vectorized_word_to_pdf.pdf"
output_txt = "./fitz_easyocr_text.txt"

# Create OCR reader
reader = easyocr.Reader(['es', 'en'])
doc = fitz.open(pdf_path)
output_text = ""

for page_num, page in enumerate(doc):
    print(f"Processing page {page_num + 1}/{len(doc)}...")
    # 1. Text
    text = page.get_text()
    output_text += f"\n--- TEXT PAGE {page_num + 1} ---\n"
    output_text += text + "\n"

    # 2. Images
    image_list = page.get_images(full=True)
    if image_list:
        output_text += f"\n--- OCR IMAGES PAGE {page_num + 1} ---\n"

    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]

        # Save OCR
        ocr_result = reader.readtext(image_bytes, detail=0)
        output_text += f"\nImage {img_index + 1} OCR:\n"
        output_text += "\n".join(ocr_result) + "\n"

# Save txt file
with open(output_txt, "w", encoding="utf-8") as f:
    f.write(output_text)

print("Text saved in:", output_txt)

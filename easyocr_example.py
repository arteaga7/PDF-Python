#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:           easyocr_example.py
Author:         Antonio Arteaga
Last Updated:   2025-11-18
Version:        1.0
Description:
Obtains text from an IMAGE and the coordinates where the text was found
in the picture by using the easyocr library. The coordinetas of a specific
text can be obtained by changing the 'text_condition' variable.
Dependencies:   opencv-python==4.12.0.88, easyocr==1.7.2
"""

import numpy as np
import easyocr
import cv2
from matplotlib import pyplot as plt

text_condition = 'corresp'      # Text to search for in the image
image_path = './data/raw/example1.png'

# Create the reader, specifying the language.
reader = easyocr.Reader(['es', 'en'], gpu=False)      # 'es' for Spanish

# Load image
image = cv2.imread(image_path)

# Read text
results = reader.readtext(image_path)
# results → [ [bbox, texto, prob], ... ]

# Show text found with confidence
for (bbox, text, prob) in results:
    print(f"Text: {text} (confidence: {prob:.2f})")

# Obtain the coordenates of the text found
coordinates = [bbox for (bbox, text, prob)
               in results if text_condition in text]
print(f"Coordinates of text box containing '{text_condition}':", coordinates)

# Show image with bounding boxes
for (bbox, text, prob) in results:
    pts = cv2.polylines(image, [np.int32(bbox)], True, (0, 255, 0), 2)

plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

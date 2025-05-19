# Picture to Text Converter

This Python module uses OCR (Optical Character Recognition) to extract text from image files. It leverages OpenCV for image processing and Tesseract OCR via the `pytesseract` wrapper to convert images to text.

## Features

- Reads image files (e.g., PNG, JPG) and extracts text content
- Simple class-based design for easy integration
- Uses Tesseract OCR engine through `pytesseract`

## Requirements

- Python 3.11 or 3.12
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and accessible in your system path
- Python dependencies managed via Poetry:
  - `opencv-python`
  - `pytesseract`

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd picture-to-text
```

# Picture to Text Converter

This Python module uses OCR (Optical Character Recognition) to extract text from image files. It leverages OpenCV for image processing and Tesseract OCR via the `pytesseract` wrapper to convert images to text.

## Features

- Reads image files (e.g., PNG, JPG) and extracts text content
- Simple class-based design for easy integration
- Uses Tesseract OCR engine through `pytesseract`

## Requirements

- Python 3.11 or 3.12
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and accessible in your system path
- Python dependencies managed via Poetry:
  - `opencv-python`
  - `pytesseract`

# Install system dependency — Tesseract OCR:

On Ubuntu/Debian:
```
sudo apt-get install tesseract-ocr
```
On macOS (using Homebrew):
```
brew install tesseract
```
Install Python dependencies via Poetry:
```
poetry install
```

# Usage
- Place the image file you want to extract text from (e.g., A1.png) in your working directory.
- Edit main.py (or your script) to specify the image filename:
```
doc = 'A1.png'
str = Convert(doc).get_text()
print(str)
```
Run the script using Poetry:
```
poetry run python main.py
```

# Notes 
Notes
- Ensure the image contains clear, readable text for best OCR results.
- You can preprocess images with OpenCV to improve OCR accuracy if needed.
- This tool supports any image format supported by OpenCV.

# Author
Martin Jaramillo

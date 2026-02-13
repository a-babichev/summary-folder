import pytesseract
from PIL import Image
import pdfplumber
from pdf2image import convert_from_path
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(file_path: str) -> str:
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image, lang="rus+eng")
        return text
    except Exception as e:
        print(f"OCR error for image {file_path}: {e}")
        return ""

def extract_text_from_pdf(file_path: str) -> str:
    text_content = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text_content += page.extract_text() or ""

        if not text_content.strip():
            images = convert_from_path(file_path)
            for img in images:
                text_content += pytesseract.image_to_string(img, lang="rus+eng")

    except Exception as e:
        print(f"PDF processing error {file_path}: {e}")

    return text_content

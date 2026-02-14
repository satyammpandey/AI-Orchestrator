import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# WINDOWS USERS: Ensure this path is correct for your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(file_bytes: bytes, filename: str) -> str:
    extension = filename.split('.')[-1].lower()
    text = ""

    try:
        # 1. Handle PDFs (including scanned/handwritten ones)
        if extension == 'pdf':
            doc = fitz.open(stream=file_bytes, filetype="pdf")
            for page in doc:
                # First, try to get digital text
                page_text = page.get_text().strip()
                
                # If no digital text found (it's a scan or handwriting)
                if not page_text:
                    # Convert page to an image (300 DPI for better OCR)
                    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                    img = Image.open(io.BytesIO(pix.tobytes()))
                    # Run OCR on the page image
                    page_text = pytesseract.image_to_string(img)
                
                text += page_text + "\n"
        
        # 2. Handle Images (Direct OCR)
        elif extension in ['png', 'jpg', 'jpeg']:
            image = Image.open(io.BytesIO(file_bytes))
            text = pytesseract.image_to_string(image)
            
        # 3. Handle Text files
        elif extension == 'txt':
            text = file_bytes.decode("utf-8")
            
    except Exception as e:
        return f"Error processing {filename}: {str(e)}"
    
    return f"\n--- ATTACHED FILE ({filename}) ---\n{text}\n--- END OF FILE ---"
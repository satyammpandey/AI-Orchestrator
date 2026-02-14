import PyPDF2
from typing import Optional
import os

class PDFService:
    @staticmethod
    async def extract_text(file_path: str) -> str:
        """Extract text from PDF file"""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                return text.strip()
        except Exception as e:
            raise Exception(f"PDF extraction error: {str(e)}")
    
    @staticmethod
    async def get_pdf_info(file_path: str) -> dict:
        """Get PDF metadata"""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                return {
                    "pages": len(pdf_reader.pages),
                    "metadata": pdf_reader.metadata if pdf_reader.metadata else {}
                }
        except Exception as e:
            raise Exception(f"PDF info error: {str(e)}")

pdf_service = PDFService()
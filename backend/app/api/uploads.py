from fastapi import APIRouter, UploadFile, File
from typing import List

router = APIRouter(prefix="/uploads", tags=["Uploads"])


async def upload_file(file: UploadFile = File(...)):
    # The '= File(...)' tells FastAPI this must be a real file upload
    return {
        "filename": file.filename, 
        "content_type": file.content_type,
        "status": "Uploaded successfully"
    }
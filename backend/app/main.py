from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .api import auth, tasks
from fastapi import UploadFile, File, Form
from app.utils.file_processor import extract_text
from app.api import auth # Add at top



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.options("/{rest_of_path:path}")
async def preflight(request: Request, rest_of_path: str):
    return JSONResponse(content="OK")

app.include_router(auth.router, prefix="/api/auth")
app.include_router(tasks.router, prefix="/api/tasks")
app.include_router(auth.router, prefix="/api/auth") # Add near your other routers

@app.get("/api/health")
def health():
    return {"status": "healthy"}
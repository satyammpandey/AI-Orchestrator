from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import List, Union, Any
import os

class Settings(BaseSettings):
    # API Information
    API_TITLE: str = "AI Orchestrator"
    API_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Security & Keys
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev_secret_key_123")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    
    # Database & Storage
    DATABASE_URL: str = "sqlite:///./ai_orchestrator.db"
    REDIS_URL: str = "redis://localhost:6379"
    UPLOAD_DIR: str = "./uploads"
    MAX_FILE_SIZE: int = 10485760
    
    # Allowed Origins (CORS)
    ALLOWED_ORIGINS: Union[List[str], str] = ["http://localhost:3000", "http://localhost:5173"]

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def handle_comma_separated_list(cls, v: Any) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            return v
        return ["*"]

    model_config = {
        "env_file": ".env",
        "extra": "ignore"
    }

settings = Settings()
"""
Application configuration from environment variables
"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings"""
    API_TITLE: str = "AI Curriculum Animation Platform"
    API_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    
    # Model paths
    MODEL_PATH: str = "./models/base_model"
    LORA_PATH: str = "./models/fine_tuned"
    
    # Output paths
    OUTPUT_VIDEO_PATH: str = "./outputs/videos"
    OUTPUT_AUDIO_PATH: str = "./outputs/audio"
    
    class Config:
        env_file = ".env"


settings = Settings()

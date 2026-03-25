"""
Request and response schemas
"""

from pydantic import BaseModel
from typing import Optional, Dict, Any


class GenerationRequest(BaseModel):
    """Schema for content generation request"""
    prompt: str
    parameters: Optional[Dict[str, Any]] = None


class GenerationResponse(BaseModel):
    """Schema for content generation response"""
    content: str
    status: str
    metadata: Optional[Dict[str, Any]] = None

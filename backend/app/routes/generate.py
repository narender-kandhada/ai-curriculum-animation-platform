"""
Content generation routes
"""

from fastapi import APIRouter, HTTPException
from schemas.request_response import GenerationRequest, GenerationResponse
from services.model_service import ModelService

router = APIRouter(prefix="/api", tags=["generation"])
model_service = ModelService()


@router.post("/generate", response_model=GenerationResponse)
async def generate_content(request: GenerationRequest):
    """Generate curriculum animation content"""
    try:
        result = await model_service.generate(request.prompt, **request.parameters)
        return GenerationResponse(
            content=result,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

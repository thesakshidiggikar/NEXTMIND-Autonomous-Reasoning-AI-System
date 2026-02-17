from fastapi import APIRouter
from api.schemas import PipelineRequest, PipelineResponse
from core.pipeline import NextMindPipeline

router = APIRouter()
pipeline = NextMindPipeline()


@router.post("/run", response_model=PipelineResponse)
def run_nextmind(request: PipelineRequest):
    result = pipeline.run({
        "uncertainty": request.uncertainty,
        "novelty": request.novelty or 0.0,
        "embedding": request.embedding
    })
    return result

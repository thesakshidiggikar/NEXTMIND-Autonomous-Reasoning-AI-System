from pydantic import BaseModel

class PipelineRequest(BaseModel):
    uncertainty: float
    novelty: float

class PipelineResponse(BaseModel):
    curiosity_score: float
    hypothesis: str
    analysis_decision: str
    meta_decision: str

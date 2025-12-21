from pydantic import BaseModel
from typing import Any, List, Dict

class AnalysisResponse(BaseModel):
    url: str
    platform: str
    analysis: Dict[str, Any]

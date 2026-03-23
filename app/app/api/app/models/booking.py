from pydantic import BaseModel, Field
from typing import List, Optional

class Talent(BaseModel):
    name: str
    alignment: str = Field(description="heel, face, tweener")
    faction: Optional[str] = None
    champion: bool = False
    availability_score: int = 100
    momentum_score: int = 50

class MatchRequest(BaseModel):
    show_name: str
    city: str
    event_date: str
    roster: List[Talent]
    match_count: int = 6
    include_title_match: bool = True
    notes: Optional[str] = None

class MatchCardItem(BaseModel):
    slot: int
    stipulation: str
    participants: List[str]
    rationale: str
    continuity_notes: List[str] = []

class MatchCardResponse(BaseModel):
    show_name: str
    matches: List[MatchCardItem]
    warnings: List[str] = []

from typing import List
from app.models.booking import Talent

def filter_available_talent(roster: List[Talent]) -> List[Talent]:
    return [talent for talent in roster if talent.availability_score >= 70]

def separate_by_alignment(roster: List[Talent]) -> tuple[list[Talent], list[Talent], list[Talent]]:
    heels = [t for t in roster if t.alignment == "heel"]
    faces = [t for t in roster if t.alignment == "face"]
    tweeners = [t for t in roster if t.alignment == "tweener"]
    return heels, faces, tweeners

def identify_champions(roster: List[Talent]) -> List[Talent]:
    return [talent for talent in roster if talent.champion]

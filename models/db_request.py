from pydantic import BaseModel
from typing import Optional, Dict

class DatabaseRequest(BaseModel):
    zapotec: str
    gloss: str
    english: str
    text_file: str
    line_number: Optional[int]
    morphemes: Optional[Dict]
    comments: Optional[dict]


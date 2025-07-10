from pydantic import BaseModel
from typing import Optional, Dict

class SentenceRequest(BaseModel):
    text_file: str
    line_number: Optional[int]
    zapotec: str
    gloss: str
    english: str

    morphemes: Optional[Dict]
    comments: Optional[str]


class GlossRequest(BaseModel):
    gloss:str
    definition:str


class BibleRequest(BaseModel):
    book:str
    chapter:int
    verse:int
    zapotec:str
    gloss:str
    english:str
    morphemes:Optional[dict]
    comments:Optional[str]
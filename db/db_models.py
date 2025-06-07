from sqlalchemy import Column, Integer, String, JSON, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ZapotecSentence(Base):
    __tablename__ = "zapotec_sentences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    zapotec = Column(String, nullable=False)
    gloss = Column(String, nullable=False)
    english = Column(String, nullable=False)
    text_file = Column(String, nullable=False)
    line_number = Column(Integer)
    morphemes = Column(JSON)
    comments = Column(String)

class GlossDictionary(Base):
    __tablename__ = "gloss_dictionary"

    gloss = Column(String, primary_key=True)
    definition = Column(String, nullable=False)

# create indices
Index("ix_text_file", ZapotecSentence.text_file)
Index("ix_line_number", ZapotecSentence.line_number)


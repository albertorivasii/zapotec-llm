from sqlalchemy import Column, Integer, String, JSON, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ZapotecSentence(Base):
    __tablename__ = "zapotec_sentences"

    text_file = Column(String, nullable=False)
    line_number = Column(Integer)
    id = Column(Integer, primary_key=True, autoincrement=True)
    zapotec = Column(String, nullable=False)
    gloss = Column(String, nullable=False)
    english = Column(String, nullable=False)
    morphemes = Column(JSON)
    comments = Column(String)

class GlossDictionary(Base):
    __tablename__ = "gloss_dictionary"

    gloss = Column(String, primary_key=True)
    definition = Column(String, nullable=False)


class BibleVerses(Base):

    __tablename__ = "bible_verses"
    verse_id= Column(Integer, primary_key=True, autoincrement=True)
    book = Column(String)
    chapter= Column(String)
    verse_num= Column(Integer)
    zapotec = Column(String)
    gloss= Column(String)
    english= Column(String)
    morphemes= Column(JSON, nullable=True)
    comments= Column(String, nullable=True)
    english:str


# create indices
Index("ix_text_file", ZapotecSentence.text_file)
Index("ix_line_number", ZapotecSentence.line_number)
Index("ix_bible_chapter", BibleVerses.chapter)
Index("ix_bible_verse", BibleVerses.verse_num)


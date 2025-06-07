from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.db_models import ZapotecSentence, GlossDictionary
from models.db_request import DatabaseRequest
from typing import List


class DatabaseHelper():
    def __init__(self, session:Session, db_url:str):
        self.session= session
        self.db_url= db_url


    def save_sentence(self, data:DatabaseRequest):
        entry= ZapotecSentence(
            zapotec= data.zapotec,
            gloss= data.gloss,
            english= data.english,
            text_file= data.text_file,
            line_number= data.line_number,
            morphemes=data.morphemes,
            comments= data.comments
        )

        self.session.add(entry)


    def get_sentence_by_id(self, sentence_id:int):
        sentence= self.session.query(
            ZapotecSentence
            ).filter(
                ZapotecSentence.id == sentence_id
            )
        return sentence.first()


    def get_sentences_by_text_file(self, text_file:str):
        sentences= self.session.query(
            ZapotecSentence
        ).filter(
            ZapotecSentence.text_file == text_file
        )

        return sentences.all()
        

    def update_sentence(self, sentence_id:int, updates:dict):
        try:
            self.session.query(ZapotecSentence).filter(
                ZapotecSentence.id == sentence_id
            ).update(
                updates
            )
        except Exception as e:
            return f"Unable to update sentence id: {id}. Error: {e}"
        return f"Sentence {id} is now updated."


    def delete_sentence(self, sentence_id: int):
        try:
            self.session.query(ZapotecSentence).filter(
                ZapotecSentence.id == sentence_id
            ).delete()
        except Exception as e:
            return f"Unable to delete sentence. Error: {e}"
        
        return f"Sentence {id} deleted successfully."

    
    def add_gloss_definition(self, gloss:str, definition:str):
        try:
            self.session.add(gloss, definition)
        except Exception as e:
            return f"Unable to add gloss definition. Error: {e}"
        return "Gloss added successfully."

    def get_gloss_definition(self, gloss:str):
        try:
            result= self.session.query(GlossDictionary).filter(
                GlossDictionary.gloss == gloss
            )
        except Exception as e:
            return f"Gloss no found. Error: {e}"
        return result.all()


    def get_all_glosses(self):
        pass


    def insert_sentences(self, data_list: List[DatabaseRequest]):
        pass

    
    def to_csv(self, filename:str):
        pass


    def from_csv(self, filename:str):
        pass

    def close(self):
        self.session.close()
        return "Connection Closed."
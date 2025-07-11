from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.db_models import ZapotecSentence, GlossDictionary
from models.db_request import DatabaseRequest
from typing import List
import pandas as pd


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
        raise RuntimeError(f"Sentence {id} is now updated.")


    def delete_sentence(self, sentence_id: int):
        try:
            self.session.query(ZapotecSentence).filter(
                ZapotecSentence.id == sentence_id
            ).delete()
        except Exception as e:
            raise RuntimeError(f"Unable to delete sentence. Error: {e}")
        
        return f"Sentence {id} deleted successfully."

    
    def add_gloss_definition(self, gloss:str, definition:str):
        try:
            self.session.add(gloss, definition)
        except Exception as e:
            raise RuntimeError(f"Unable to add gloss definition. Error: {e}")
        return "Gloss added successfully."

    def get_gloss_definition(self, gloss:str):
        try:
            result= self.session.query(GlossDictionary).filter(
                GlossDictionary.gloss == gloss
            )
        except Exception as e:
            raise RuntimeError(f"Gloss no found. Error: {e}")
        return result.all()


    def get_all_glosses(self):
        try:
            glosses= self.session.query(GlossDictionary)
            return glosses.all()
        except Exception as e:
            raise RuntimeError(f"Error getting Gloss Table. Error: {e}")


    def insert_sentences(self, data_list: List[DatabaseRequest]):
        try:
            # Convert DatabaseRequest objects to ZapotecSentence objects
            entries = [
                ZapotecSentence(
                    zapotec=data.zapotec,
                    gloss=data.gloss,
                    english=data.english,
                    text_file=data.text_file,
                    line_number=data.line_number,
                    morphemes=data.morphemes,
                    comments=data.comments
                )
                for data in data_list
            ]

            self.session.add_all(entries)

        except Exception as e:
            raise RuntimeError(f"Cannot add all entries. Error: {e}")

        return f"Added {len(entries)} entries to ZapotecSentences"

    
    def to_csv(self, filename:str, table:str):
        if table.lower() == "sentences":
            try:
                results= self.session.query(ZapotecSentence)
                df= pd.DataFrame(results.all())
                df.to_csv(filename)
                return f"{table} successfully saved to {filename}"
            except Exception as e:
                raise ValueError(f"Unable to convert {table} to csv. Error: {e}")
        elif table.lower() == "sentences":
            try:
                results= self.session.query(GlossDictionary)
                df= pd.DataFrame(results.all())
                df.to_csv(filename)
            except Exception as e:
                raise ValueError(f"Unable to convert {table} to csv. Error: {e}")
            return f"{table} successfully saved to {filename}"    
        

    def from_csv(self, filename: str, table: str) -> str:
        try:
            df = pd.read_csv(filename)

            if table.lower() == "sentences":
                entries = [
                    ZapotecSentence(
                        zapotec=row["zapotec"],
                        gloss=row["gloss"],
                        english=row["english"],
                        text_file=row.get("text_file"),
                        line_number=row.get("line_number"),
                        morphemes=row.get("morphemes"),  # JSON string if present
                        comments=row.get("comments")
                    )
                    for _, row in df.iterrows()
                ]

            elif table.lower() == "gloss":
                entries = [
                    GlossDictionary(
                        gloss=row["gloss"],
                        definition=row["definition"]
                    )
                    for _, row in df.iterrows()
                ]

            else:
                return f"Unknown table name: {table}"

            self.session.add_all(entries)

            return f"Successfully added {len(entries)} entries to the {table} table."

        except Exception as e:
            raise RuntimeError(f"Error during CSV import: {e}")


    def commit(self):
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RuntimeError(f"Error committing changes. Rolling back any changes. Error: {e}")

    def close(self):
        self.session.close()
        return "Connection Closed."
    
    
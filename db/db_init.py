from sqlalchemy import create_engine
from db_models import Base

def init_db():
    engine= create_engine("sqlite:///zapotec_data.db")
    try:
        Base.metadata.create_all(engine)
        #return "Database initialized successfully."
        print("Database initialized successfully.")
    except Exception as e:
        raise ValueError(f"Database Initialization failed. Error: {e}")
    
if __name__ == "__main__":
    init_db()
from src.database import db
from src.app import app

test_app = app
test_app.app_context().push()

def create_tables():
    db.session.execute("""
        CREATE TABLE IF NOT EXISTS Viitteet (
            id SERIAL PRIMARY KEY,
            viite TEXT,
            tyyppi TEXT,
            vuosi INTEGER,
            kirjailija TEXT,
            otsikko TEXT,
            kustantaja TEXT,
            versio INTEGER,
            julkaisunumero TEXT,
            sivut TEXT
        );
    """)
    db.session.commit()

def empty_tables():
    db.session.execute("""
        TRUNCATE TABLE IF EXISTS Viitteet CASCADE;
    """)
    db.session.commit()

def initialize_database():
    empty_tables()
    create_tables()
    
if __name__ == "__main__":
    initialize_database()
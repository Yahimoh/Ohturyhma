from src.database import db
from src.app import app

test_app = app
test_app.app_context().push()

def create_tables():
    db.session.execute("""
        CREATE TABLE Viitteet (
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

def drop_tables():
    db.session.execute("""
        DROP TABLE IF EXISTS KirjaViitteet;
        DROP TABLE IF EXISTS Viitteet;
    """)
    db.session.commit()

def initialize_database():
    drop_tables()
    create_tables()
    
if __name__ == "__main__":
    initialize_database()
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from src.viite import Viite

db = SQLAlchemy()

def lisaa_viite(viite: Viite):
    sql = text("""
            INSERT INTO
                KirjaViitteet (viite, kirjailija, otsikko, vuosi, kustantaja)
            VALUES
                (:viite, :kirjailija, :otsikko, :vuosi, :kustantaja);
            """)
    db.session.execute(sql, {
        "viite":       viite.tiedot["nimi"],
        "kirjailija":  viite.tiedot["kirjailija"],
        "otsikko":     viite.tiedot["otsikko"],
        "vuosi":       viite.tiedot["vuosi"], 
        "kustantaja":  viite.tiedot["kustantaja"]
    })
    db.session.commit()

def lue_viitteet():
    sql = text("SELECT * FROM KirjaViitteet;")
    vastaus = db.session.execute(sql)
    return [Viite(x) for x in vastaus.mappings().all()]
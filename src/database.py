import copy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from src.viite import Viite

db = SQLAlchemy()

lisattavat = [
    "viite", "tyyppi", "kirjailija", "otsikko", "vuosi", "kustantaja", "julkaisunumero", "sivut"
]

def lisaa_viite(viite: Viite):
    sql = text("""
            INSERT INTO
                Viitteet (viite, tyyppi, kirjailija, otsikko, vuosi, kustantaja, julkaisunumero, sivut)
            VALUES
                (:viite, :tyyppi, :kirjailija, :otsikko, :vuosi, :kustantaja, :julkaisunumero, :sivut)
            RETURNING
               id;""")
    d = {}
    for lisattava in lisattavat:
        d[lisattava] = viite.tiedot.get(lisattava, None)

    vastaus = db.session.execute(sql, d)
    id = vastaus.fetchone()[0]
    db.session.commit()

    uusi_viite = copy.deepcopy(viite)
    uusi_viite.tiedot["id"] = id
    return uusi_viite

def lue_viitteet():
    sql = text("SELECT * FROM Viitteet;")
    vastaus = db.session.execute(sql)
    return [Viite(x) for x in vastaus.mappings().all()]

def poista_viite(id):
    sql = text("""
            DELETE FROM
                Viitteet
            WHERE
                id = :id;
            """)

    db.session.execute(sql, {"id": id})
    db.session.commit()

def poista_kaikki_viitteet():
    sql = text("TRUNCATE Viitteet CASCADE;")
    db.session.execute(sql)
    db.session.commit()
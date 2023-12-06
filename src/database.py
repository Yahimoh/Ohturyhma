import copy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from src.viite import Viite

db = SQLAlchemy()

lisattavat = [
    "viite", "tyyppi", "kirjailija", "otsikko", "vuosi", "kustantaja", "julkaisunumero", "sivut"
]

def lisaa_viite(viite: Viite):
    viite = tarkasta_viiteavain_unique(viite)
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
    viite_id = vastaus.fetchone()[0]
    db.session.commit()

    uusi_viite = copy.deepcopy(viite)
    uusi_viite.tiedot["id"] = viite_id
    return uusi_viite

def lue_viitteet():
    sql = text("SELECT * FROM Viitteet;")
    vastaus = db.session.execute(sql)
    return [Viite(x) for x in vastaus.mappings().all()]

def etsi_viite(viite_id: int):
    sql = text("SELECT * FROM Viitteet WHERE id = :id;")
    vastaus = db.session.execute(sql, {"id": viite_id})
    return Viite(vastaus.mappings().all()[0])

def poista_viite(viite_id):
    sql = text("""
            DELETE FROM
                Viitteet
            WHERE
                id = :id;
            """)

    db.session.execute(sql, {"id": viite_id})
    db.session.commit()

def poista_viite_tyyppi(tyyppi):
    sql = text("""
            DELETE FROM
                Viitteet
            WHERE
                tyyppi = :tyyppi;
            """)

    db.session.execute(sql, {"tyyppi": tyyppi})
    db.session.commit()

def poista_kaikki_viitteet():
    sql = text("TRUNCATE Viitteet CASCADE;")
    db.session.execute(sql)
    db.session.commit()

def tarkasta_viiteavain_unique(viite: Viite):
    alkuperainen_viite = viite.tiedot.get("viite", "")
    uusi_viite = alkuperainen_viite
    aakkoset = "abcdefghijklmnopqrstuvwxyz"
    kirjain_index = 0

    while True:
        sql = text("SELECT COUNT(*) FROM Viitteet WHERE viite = :viite;")
        result = db.session.execute(sql, {"viite": uusi_viite}).scalar()

        if result == 0:            
            break
        else:            
            if kirjain_index < len(aakkoset):
                uusi_viite = alkuperainen_viite + aakkoset[kirjain_index]
                kirjain_index += 1
            else:                
                uusi_viite = alkuperainen_viite + aakkoset[kirjain_index // len(aakkoset) - 1] + aakkoset[kirjain_index % len(aakkoset)]
                kirjain_index += 1

    viite.tiedot["viite"] = uusi_viite
    return viite
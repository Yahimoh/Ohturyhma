from sqlalchemy.sql import text
from src.viite import Viite
from src.db import db

lisattavat = [
    "viite", "tyyppi", "kirjailija", "otsikko", "vuosi", "kustantaja", "julkaisunumero", "sivut"
]

def lisaa_viite(viite: Viite):
    viite = tarkasta_viiteavain_unique(viite)
    sql = text("""
            INSERT INTO
                Viitteet (viite, tyyppi, kirjailija, otsikko, vuosi, kustantaja, julkaisunumero, sivut)
            VALUES
                (:viite, :tyyppi, :kirjailija, :otsikko, :vuosi, :kustantaja, :julkaisunumero, :sivut);""")
    data = {}
    for lisattava in lisattavat:
        data[lisattava] = viite.tiedot.get(lisattava, None)

    db.session.execute(sql, data)
    db.session.commit()

def lue_viitteet(tyyppi=None):
    if tyyppi is None:
        sql = text("SELECT * FROM Viitteet ORDER BY id;")
    else:
        sql = text("SELECT * FROM Viitteet WHERE tyyppi = :tyyppi ORDER BY id;")
    vastaus = db.session.execute(sql, {"tyyppi": tyyppi})
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
    sql = text("TRUNCATE Viitteet;")
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

        if kirjain_index < len(aakkoset):
            uusi_viite = alkuperainen_viite + aakkoset[kirjain_index]
            kirjain_index += 1
        else:                
            uusi_viite = alkuperainen_viite + aakkoset[kirjain_index // len(aakkoset) - 1] + aakkoset[kirjain_index % len(aakkoset)]
            kirjain_index += 1

    viite.tiedot["viite"] = uusi_viite
    return viite
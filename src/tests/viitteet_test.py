import unittest
from sqlalchemy.sql import text
from src.initialize_database import initialize_database
from src.database import db, lisaa_viite, poista_viite, poista_kaikki_viitteet, lue_viitteet
from src.viite import Viite, maarita_nimi

def pytest_configure():
    initialize_database()

class TestApp(unittest.TestCase):
    def setUp(self):
        sql = text('TRUNCATE TABLE Viitteet')
        db.session.execute(sql)

    def test_lisaa_kirja(self):
        viite = Viite({
            "tyyppi": "book",
            "kirjailija": 'kirjailija',
            "otsikko": "otsikko",
            "vuosi": 2023,
            "kustantaja": "kustantaja",
            "viite": maarita_nimi("kirjailija", "vuosi")
        })
        kirja = lisaa_viite(viite)
        self.assertTrue(kirja)
        
    def test_lisaa_artikkeli(self):
        viite = Viite({
            "tyyppi": "article",
            "kirjailija": 'kirjailija',
            "otsikko": "otsikko",
            "vuosi": 2023,
            "julkaisunumero": 15,
            "kustantaja": "kustantaja",
            "sivut": 10,
            "viite": maarita_nimi("kirjailija", "vuosi")
        })
        artikkeli = lisaa_viite(viite)
        self.assertTrue(artikkeli)
        
    def test_poista_viitteet(self):
        kirjaviite = Viite({
            "tyyppi": "book",
            "kirjailija": 'testikirjailija',
            "otsikko": "testiotsikko",
            "vuosi": 2023,
            "kustantaja": "testikustantaja",
            "viite": maarita_nimi("kirjailija", "vuosi")
        })
        lisaa_viite(kirjaviite)
        artikkeliviite = Viite({
            "tyyppi": "article",
            "kirjailija": 'kirjailija',
            "otsikko": "otsikko",
            "vuosi": 2023,
            "julkaisunumero": 15,
            "kustantaja": "kustantaja",
            "sivut": 10,
            "viite": maarita_nimi("kirjailija", "vuosi")
        })
        lisaa_viite(artikkeliviite)
        poista_kaikki_viitteet()
        viitteet = lue_viitteet()
        self.assertEqual(viitteet, [])
        
    def test_poista_viite(self):
        kirjaviite = Viite({
            "tyyppi": "book",
            "kirjailija": 'testikirjailija',
            "otsikko": "testiotsikko",
            "vuosi": 2023,
            "kustantaja": "testikustantaja",
            "viite": maarita_nimi("kirjailija", "vuosi")
        })
        lisaa_viite(kirjaviite)
        viitteet = lue_viitteet()
        poista_viite(viitteet[0].tiedot['id'])
        viitteet_nyt = lue_viitteet()
        self.assertEqual(viitteet_nyt, [])
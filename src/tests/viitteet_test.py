import unittest
import src.initialize_database
from src.viite import Viite, maarita_nimi
import src.database as data

class TestApp(unittest.TestCase):
    def setUp(self):
        data.poista_kaikki_viitteet()

    def test_lisaa_kirja(self):
        viite = Viite({
            "tyyppi": "book",
            "kirjailija": 'kirjailija',
            "otsikko": "otsikko",
            "vuosi": 2023,
            "kustantaja": "kustantaja",
            "viite": maarita_nimi("kirjailija", "vuosi")
        })
        kirja = data.lisaa_viite(viite)
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
        artikkeli = data.lisaa_viite(viite)
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
        data.lisaa_viite(kirjaviite)
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
        data.lisaa_viite(artikkeliviite)
        data.poista_kaikki_viitteet()
        viitteet = data.lue_viitteet()
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
        data.lisaa_viite(kirjaviite)
        viitteet = data.lue_viitteet()
        data.poista_viite(viitteet[0].tiedot['id'])
        viitteet_nyt = data.lue_viitteet()
        self.assertEqual(viitteet_nyt, [])
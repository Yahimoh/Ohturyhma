from src.viite import Viite, maarita_nimi
import unittest

class ViiteTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_viite_ilmaistaan_merkkijonona(self):
        data = {"viite": "blabla", "tyyppi": "book", "otsikko": "vastaus2", "kirjailija": "joku", "vuosi": 123, "kustantaja": "jokin"}
        viite = Viite(data)
        self.assertEqual(str, type(viite.__str__()))

    def test_viitteella_tieto_sanakirjana(self):
        data = {"viite": "blabla", "tyyppi": "article", "otsikko": "vastaus2", "kirjailija": "joku", "vuosi": 123, "kustantaja": "jokin"}
        viite = Viite(data)
        self.assertEqual(dict, type(viite.tiedot))

    def test_maarita_nimi_yksi_tekija(self):
        self.assertEqual(maarita_nimi("Joe Smith", 2020), "S20")

    def test_maarita_nimi_monta_tekijaa(self):
        self.assertEqual(maarita_nimi("Sam Smith, Pekka Pouta and Joe Doe", 2023), "SPD23")

    def test_maarita_nimi_tekijat_erotettu_eri_tavoilla(self):
        self.assertEqual(maarita_nimi("Sam Smith, Pekka Pouta and Joe Doe ja Tapsa Jormakka", 2021), "SPDJ21")
    


    
    
    
    

    

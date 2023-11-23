from src.viite import Viite
import unittest

class ViiteTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_viite_ilmaistaan_merkkijonona(self):
        data = {"esim": "vastaus", "esim2": "vastaus2"}
        viite = Viite(data)
        self.assertEqual(str, type(viite.__str__()))

    def test_viitteella_tieto_sanakirjana(self):
        data = {"viite": "vastaus", "otsikko": "vastaus2", "kirjailija": "joku", "vuosi": 123, "kustantaja": "jokin"}
        viite = Viite(data)
        self.assertEqual(dict, type(viite.tiedot))


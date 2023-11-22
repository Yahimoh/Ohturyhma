from src.viite import ViiteLista, Viite
import unittest

class ViiteTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_viite_ilmaistaan_merkkijonona(self):
        data = {"esim": "vastaus", "esim2": "vastaus2"}
        viite = Viite(data)
        self.assertEqual(str, type(viite.__str__()))

    def test_viitteella_tieto_sanakirjana(self):
        data = {"esim": "vastaus", "esim2": "vastaus2"}
        viite = Viite(data)
        self.assertEqual(dict, type(viite.tiedot))

class ViiteListaTest(unittest.TestCase):
    def setUp(self):
        self.viite = Viite({"esim": "vastaus", "esim2": "vastaus2"})

    def test_viitelistaan_voi_lisaa_viitteen(self):
        lista = ViiteLista()
        lista.lisaa_viite(self.viite)

        self.assertEqual(1, len(lista.viitteet))

    def test_viitelista_palauttaa_viitteet_merkkijonona(self):
        lista = ViiteLista()
        lista.lisaa_viite(self.viite)

        tulostus = lista.hae_viitelista()

        self.assertEqual(str, type(tulostus[0]))


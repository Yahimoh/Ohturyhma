import unittest
from src.validators import syotteen_tarkastus, SyoteVirhe
from src.viite import Viite

class TestSyotteenTarkastus(unittest.TestCase):

    def test_kelpo_syote(self):
        viite = Viite({
        "tyyppi": "book",
        "kirjailija": 'Pekka Pouta',
        "otsikko": 'Jepp',
        "vuosi": 2023,
        "kustantaja": 'WSOY',
        "viite": '12OB'})
    
        self.assertTrue(syotteen_tarkastus(viite))

    def test_liian_pitka_syote(self):
        viite = viite = Viite({
        "tyyppi": "book",
        "kirjailija": 'a' * 101,
        "otsikko": 'Jepp',
        "vuosi": 2023,
        "kustantaja": 'WSOY',
        "viite": '12OB'})
        
        with self.assertRaises(SyoteVirhe):
            syotteen_tarkastus(viite)

    def test_liian_lyhyt_syote(self):
        viite = viite = Viite({
        "tyyppi": "book",
        "kirjailija": '',
        "otsikko": 'Jepp',
        "vuosi": 2023,
        "kustantaja": 'WSOY',
        "viite": '12OB'})

        with self.assertRaises(SyoteVirhe):
            syotteen_tarkastus(viite)

            
if __name__ == '__main__':
    unittest.main()

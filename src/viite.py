
class Viite:
    """Luokka yhdelle viitteelle. 
    """
    def __init__(self, tiedot: dict):
        """Alustuksen yhteydessä anna
        viittauksen tiedot.

        Args:
            tiedot (dict): sanakirja muotoa {"nimi": "esimerkki"}
        """
        self.tiedot = tiedot

    def __str__(self) -> str:
        """Esittää viitteen tiedot bibtex-muodossa.
        Automaattisesti rakentaa oikeanlaisen muodon
        sanakirjan perusteella.
        """
        # Yahia muuta tämä siten, että oikean näköinen bibtex-muoto
        viite = ""
        for avain, tieto in self.tiedot.items():
            viite += f"{avain}: {tieto}"
            viite += "\n"
        return viite

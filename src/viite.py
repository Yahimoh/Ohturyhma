
class Viite:
    """Luokka yhdelle viitteelle. 
    """
    def __init__(self, viitetyyppi: str, nimi: str, tiedot: dict):
        """Alustuksen yhteydessä anna
        viittauksen tiedot.
        Viitteen tyyppi ja nimi tulee antaa argumenttina.

        Args:
            tiedot (dict): sanakirja muotoa {"nimi": "esimerkki"}
        """
        self.viitetyyppi = viitetyyppi
        self.nimi = nimi
        self.tiedot = tiedot

    def __str__(self) -> str:
        """Esittää viitteen tiedot bibtex-muodossa.
        Automaattisesti rakentaa oikeanlaisen muodon
        sanakirjan perusteella.
        """
        viite = "@" + self.viitetyyppi + "{" + self.nimi + ",\n"

        for avain, arvo in self.tiedot.items():
            viite += f"{avain:12} = {{{arvo}}},\n"

        viite = viite[:-2] + viite[-1:]
        viite += "}"
        return viite
    
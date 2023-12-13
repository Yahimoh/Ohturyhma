from src.viite import Viite

class SyoteVirhe(Exception):
    def __init__(self, virheet):
        self.virheet = virheet

def syotteen_tarkastus(viite: Viite):   
    virheet = []
    for avain, arvo in viite.tiedot.items():
        arvo = str(arvo)
        if avain == "tyyppi":
            continue
        if len(arvo) < 1 or len(arvo) > 100:
            virheet.append(f"Kentän '{avain}' syöte tulee olla vähintään 1 ja enintään 100 merkkiä pitkä!")    

    if virheet:
        raise SyoteVirhe(virheet)
            
    return True
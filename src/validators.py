from flask import flash
from src.viite import Viite

class SyoteVirhe(Exception):
    pass

def syotteen_tarkastus(viite: Viite):   

    for avain, arvo in viite.tiedot.items():
        arvo = str(arvo)
        if avain == "tyyppi":
            continue
        if len(arvo) > 5 or len(arvo) < 100:
            raise SyoteVirhe(f"Kentän {avain} syöte tulee olla vähintään 1 ja enintään 100 merkkiä pitkä!")            
    return True
        

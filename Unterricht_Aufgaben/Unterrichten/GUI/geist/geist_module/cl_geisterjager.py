from typing import List
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geist import Geist


class Geisterjaeger:
    def __init__(self, name: str):
        self._name = name
        self._gefangene_geister: List[Geist] = []
        
    def geist_fangen(self, geist: Geist) -> bool: 
        if geist.sichtbar is True and geist.gefangen is False:
            geist.gefangen = True
            self._gefangene_geister.append(geist)
            #print(f"Geisterjäger: {self._name} hat {geist.name} gefangen.")
            return True
        
        return False
    
    def __str__(self):
        return f"Geisterjäger: {self._name} hat {len(self._gefangene_geister)} gefangen"

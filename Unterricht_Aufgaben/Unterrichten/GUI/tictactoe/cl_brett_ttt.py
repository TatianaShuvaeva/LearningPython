from abc import ABC, abstractmethod
from typing import List
#import random


class TicTacToe:
    def __init__(self):
        # self.spielfeld = [[str(i)]*3 for i in range(3)]
        self.spielfeld = []
        self.spielfeld.append(['1', '2','3'])
        self.spielfeld.append(['4', '5','6'])
        self.spielfeld.append(['7', '8','9'])
        self.gewinnkombinationen = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
      
        self.spielzugnummer = 1
        
    def get(self) -> List[List[str]]:
        return self.spielfeld
    
    @property
    def spieler_nummer(self):
        if self.spielzugnummer %2 == 1:
            return 1
        return 2

    def set(self, nummer: int) -> None:
        if nummer == 1:
            self._set_feld(0,0) 
        if nummer == 2:
            self._set_feld(0,1) 
        if nummer == 3:
            self._set_feld(0,2)
        if nummer == 4:
            self._set_feld(1,0) 
        if nummer == 5:
            self._set_feld(1,1) 
        if nummer == 6:
            self._set_feld(1,2) 
        if nummer == 7:
            self._set_feld(2,0)
        if nummer == 8:
            self._set_feld(2,1)
        if nummer == 9:
            self._set_feld(2,2)

    def _set_feld(self, zeile, spalte):
        
        if self.spielfeld[zeile][spalte] == "x" or self.spielfeld[zeile][spalte] == "o":
            raise Exception("Diese Zelle ist bereits gefüllt")
        
        zeichnen = None
        if self.spieler_nummer == 1:
            
            zeichnen = "x"
        else:
            zeichnen = "o"
        self.spielfeld[zeile][spalte] = zeichnen
        self.spielzugnummer += 1
        
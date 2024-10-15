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
        
    def get(self) -> List[List[str]]:
        return self.spielfeld

    def set(self, nummer: int) -> None:
        if nummer == 1:
            self.spielfeld[0][0] = 'x'
        if nummer == 2:
            self.spielfeld[0][1] = 'x'
        if nummer == 3:
            self.spielfeld[0][2] = 'x'
        if nummer == 4:
            self.spielfeld[1][0] = 'x'
        if nummer == 5:
            self.spielfeld[1][1] = 'x'
        if nummer == 6:
            self.spielfeld[1][2] = 'x'
        if nummer == 7:
            self._set_feld(2,0)
        if nummer == 8:
             self._set_feld(2,1)
        if nummer == 9:
             self._set_feld(2,2)

    def _set_feld(self, zeile, spalte):
        if self.spielfeld[zeile][spalte] != "x":
            self.spielfeld[zeile][spalte] = 'x'
        else:
            raise Exception("Diese Zelle ist bereits gefüllt")
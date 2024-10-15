from abc import ABC, abstractmethod
from typing import List


class Brett(ABC):

    @abstractmethod
    def zeige_brett(self):
        pass

    @abstractmethod
    def mache_zug(self, position):
        pass

    @abstractmethod
    def pruefe_gewinners(self):
        pass

    @abstractmethod
    def pruefe_unentschieden(self):
        pass


class TicTacToe(Brett):
    def __init__(self):
        self.spielfeld = [[" "]*3]*3
        self.gewinnkombinationen = 
        

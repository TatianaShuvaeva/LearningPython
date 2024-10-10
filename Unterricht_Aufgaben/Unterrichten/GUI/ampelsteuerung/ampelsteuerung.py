from abc import ABC, abstractmethod
from typing import List


class Ampeln(ABC):

    @abstractmethod
    def umschalten(self):
        pass

    @property
    @abstractmethod
    def farbe(self) -> str:
        pass


class AutoAmpel(Ampeln):
    def __init__(self):
        self.farben: List[str] = ["rot", "rot-gelb", "gelb", "grün"]
        self._index: int = 0

    def umschalten(self):
        self._index += 1
        if self._index > len(self.farben)-1:
            self._index = 0

    @property
    def farbe(self) -> str:
        farbe = self.farben[self._index]
        return farbe


class FussgaengerAmpel(Ampeln):
    def __init__(self):
        self.farben: List[str] = ["rot", "grün"]
        self._index: int = 0

    def umschalten(self):
        self._index += 1
        if self._index > len(self.farben)-1:
            self._index = 0

    @property
    def farbe(self) -> str:
        farbe = self.farben[self._index]
        return farbe

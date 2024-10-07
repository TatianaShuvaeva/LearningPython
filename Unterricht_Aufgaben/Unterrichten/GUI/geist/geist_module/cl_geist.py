import datetime


class Geist:
    def __init__(self, name: str, groesse: int):
        self.name = name
        self.groesse = groesse
        self._sichtbarkeitszeit: int = 10
        self._startzeit_sichtbarkeit: datetime.datetime = datetime.datetime(1984, 1, 1)
        self.gefangen = False

    @property
    def sichtbar(self) -> bool:
        now = datetime.datetime.now()
        if self._startzeit_sichtbarkeit + datetime.timedelta(seconds=self._sichtbarkeitszeit) > now:
            return True
        return False
    
    def _sichtbar_machen(self):
        now = datetime.datetime.now()
        self._startzeit_sichtbarkeit: datetime.datetime = now
    
    def spuken(self) -> str:
        return (f"sorgt für eine unheimliche Kälte im Raum.")

    def __str__(self) -> str:
        return f"Geist: {self.name} ist {self.groesse} m groß."

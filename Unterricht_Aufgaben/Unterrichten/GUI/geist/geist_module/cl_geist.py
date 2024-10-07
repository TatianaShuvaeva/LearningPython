class Geist:
    def __init__(self, name: str, groesse: int):
        self.name = name
        self.groesse = groesse
        self.sichtbar = False
        self.gefangen = False

    def spuken(self) -> str:
        return (f"sorgt für eine unheimliche Kälte im Raum.")

    def __str__(self) -> str:
        return f"Geist: {self.name} ist {self.groesse} m groß."

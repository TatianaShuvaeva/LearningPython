class Geist:
    def __init__(self, name: str, groesse: int):
        self.name= name
        self.groesse= groesse

    def spucken(self):
        return (f"sorgt für eine unheimliche Kälte im Raum.")

    def __str__(self):
        return f"Geist: {self.name} ist {self.groesse} m groß."
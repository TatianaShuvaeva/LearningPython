class Geist:
    def __init__(self, name, groesse):
        self.name= name
        self.groesse= groesse

    def spucken(self):
        print (f"Geist: {self.name} sorgt für eine unheimliche Kälte im Raum.")

    def __str__(self):
        return f"Geist: {self.name} ist {self.groesse} m groß."
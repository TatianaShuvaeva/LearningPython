from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geist import Geist


class Geisterjunge(Geist):

    def __init__(self, name, groesse):
        super(Geisterjunge, self).__init__(name, groesse)

    def spuken(self):
        return (f"schaltet das Licht aus und hinterlässt alles in Dunkelheit.")

    def sichtbar_machen(self, geist: Geist):
        geist._sichtbar_machen()

    def __str__(self):
        return f"Geisterjunge: {self.name} ist {self.groesse} m groß."

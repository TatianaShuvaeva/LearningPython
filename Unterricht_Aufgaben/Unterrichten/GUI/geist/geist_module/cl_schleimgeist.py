from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geist import Geist


class Schleimgeist(Geist):

    def __init__(self, name, groesse):
        super().__init__(name, groesse)

    def spuken(self):
        return (f"raschelt mit alten Papieren und macht gruselige Geräusche.")

    def schleimen(self):
        print(f"Schleimgeist: {self.name} : schleimt")

    def __str__(self):
        return f"Schleimgeist: {self.name}  ist {self.groesse} m groß."

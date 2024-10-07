from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geist import Geist


class Kannibalengeist(Geist):

    def __init__(self, name, groesse):
        super(Kannibalengeist, self).__init__(name, groesse)
        
    def spuken(self):
        return (f"schaltet das Licht aus und hinterlässt alles in Dunkelheit.")

    def fressen(self, anderer_geist: Geist):
        self.groesse = self.groesse + anderer_geist.groesse
        
        print(f"Kannibalengeist: {self.name} hat {anderer_geist.name} gefressen und ist nun {self.groesse} m groß!")

    def __str__(self):
        return f"Kannibalengeist: {self.name} ist {self.groesse} m groß."

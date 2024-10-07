from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geist import Geist


class Geisterjaeger(Geist):

    def __init__(self, name, groesse, sichtbar, gefangen):
        super(Geisterjaeger, self).__init__(name, groesse, sichtbar, gefangen)
        self.name_gefangene_geister = []
        
    def geist_fangen(self, geist: Geist): 
        if geist.sichtbar and not geist.gefangen:
            geist.gefangen = False
            self.name_gefangene_geister.append(geist)
            print(f"Geisterjäger: {self.name} hat {geist.name} gefangen.")

    def __str__(self):
        return f"Kannibalengeist: {self.name} ist {self.groesse} m groß."

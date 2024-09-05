#Metthodenüberladung

class Tier:
        def __init__(self, gewicht):
            self.gewicht = gewicht
        
        def ausgeben(self):
            print(f"Ich bin ein Tier und bin {self.gewicht} gr. schwer")

class Fisch(Tier):
    def __init__(self, gewicht, kiemengroesse):
        self.kiemengroesse = kiemengroesse
        super().__init__(gewicht)
    
    def ausgeben(self):
            print(f"Ich bin ein Fisch und bin {self.gewicht} gr. schwer")    

class Saeugetier(Tier):
    def __init__(self, gewicht, lungenvolumen):
        self.lungenvolumen = lungenvolumen
        super().__init__(gewicht)
    
    def ausgeben(self):
            print(f"Ich bin ein Säugetier und bin {self.gewicht} gr. schwer")     
        
        
tier_liste = [Tier(100), Fisch(200, 50), Saeugetier(500, 10)]

for t in tier_liste:
    t.ausgeben()

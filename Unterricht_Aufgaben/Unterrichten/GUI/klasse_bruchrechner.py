from tkinter import *

class Bruchrechner(Tk):
    def __init__(self):
        super().__init__()
        self.title("Bruchrechner")

        # Steuerelemente (widgets) erzeugen
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Bruch1").grid(row=1, column=1)
        Label(self, text="Bruch2").grid(row=1, column=3)
        self.ent_bruch1 = Entry(self, width=8)
        self.ent_bruch1.grid(row=2, column=1)
        self.ent_bruch2 = Entry(self, width=8)
        self.ent_bruch2.grid(row=2, column=3)

        self.btn_plus = Button(self, text="+", command=self.btn_plus_click)
        self.btn_plus.grid(row=3, column=2)

        self.lbl_ergebnis = Label(self, text="???")
        self.lbl_ergebnis.grid(row=4, column=2)

    def btn_plus_click(self):
        # aus Eingabe Bruch1 Zähler und Nenner ermitteln 
        # aus Eingabe Bruch2 Zähler und Nenner ermitteln 
        # Brüche addieren
        # ergebnis = bruch1 + bruch2
        self.lbl_ergebnis.config(text="1/2")
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geist import Geist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_schleimgeist import Schleimgeist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_kannibalengeist import Kannibalengeist

from tkinter import *


class GeistElemente(Tk):
    def __init__(self):
        super().__init__()

        self.title("GUI mit Geisten")
        self.geometry("500x400")

        self._screamer = Geist("screamer", 3, False, False)
        self._slimey = Schleimgeist("slimey", 1, False, False)
        self._bloodied_squire = Kannibalengeist("bloodied_squire", 10, False, False)
        self._fat_manic = Kannibalengeist("fat_manic", 7, False, False)

        # weitere Steuerelemente erzeugen
        self.auswaehlen_geist()

    def auswaehlen_geist(self):
        # Button
        self.btn_verwenden = Button(self, text="Verwenden", bg="gold", command=self._btn_verwenden_klick)
        self.btn_verwenden.grid(row=1, column=1, padx=5, pady=10)

        self.geister_liste = [self._screamer.name, self._slimey.name, self._bloodied_squire.name, self._fat_manic.name]
        # Variable für Radiobutton-Auswahl
        self._var_ausgewaehlte_geist = StringVar(value=self._screamer.name)
        # Radiobutton
        row = 1
        for s in self.geister_liste:
            row = row + 1
            radio_btn = Radiobutton(self, text=s, value=s, variable=self._var_ausgewaehlte_geist)
            radio_btn.grid(row=row, column=1, padx=5, pady=5, sticky="w")


    def erstellen_geist(self, geist: Geist):
        
        def klick_spuken():
            ergebnis = geist.spuken()
            self.entry.delete(0, 'end')
            self.entry.insert(0, ergebnis)

        lbl_text = str(geist)
        self.lbl_slimey = Label(self, bg="silver", text=lbl_text, width=50)
        self.lbl_slimey.grid(row=6, column=1, padx=5, pady=5)

        # Eingabefeld
        self.entry = Entry(self, bg="white", width=50)
        self.entry.grid(row=7, column=1, padx=5, pady=5)
        self.entry.insert(0, '')

        self.btn_spuken = Button(self, text="Spuken", bg="gold", command=klick_spuken)
        self.btn_spuken.grid(row=8, column=1, padx=5, pady=10)
            

    def _btn_verwenden_klick(self):
        geist_name = self._var_ausgewaehlte_geist.get()

        if geist_name == self._screamer.name:
            self.erstellen_geist(self._screamer)
            
        if geist_name == self._slimey.name:
            self.erstellen_geist(self._slimey)
            
        if geist_name == self._bloodied_squire.name:
            self.erstellen_geist(self._bloodied_squire)
        
        if geist_name == self._fat_manic.name:
            self.erstellen_geist(self._fat_manic)

from tkinter import Button, Tk, Label 
from Unterricht_Aufgaben.Unterrichten.GUI.ampelsteuerung.cl_ampelsteuerung import AutoAmpel
from PIL import Image, ImageTk


class AmpelElemente(Tk):
    def __init__(self):
        super().__init__()

        self.title("tk")
        self.geometry("432x267")

        self._ampel: AutoAmpel = AutoAmpel()
        self.wechseln_bild()
        self.erstellen_buttons()

    def erstellen_buttons(self):
        self.btn_weiter = Button(self, text="Weiter", bg="silver", command=self._btn_weiter_klick, width=12)
        self.btn_weiter.grid(row=1, column=1, padx=40, pady=45)
        
        self.btn_exit = Button(self, text="Exit", bg="silver", command=self._btn_exit_klick, width=12)
        self.btn_exit.grid(row=2, column=1, padx=40, pady=45)

    def _btn_weiter_klick(self):
        self._ampel.umschalten()
        self.wechseln_bild()
        self.erstellen_buttons()

    def wechseln_bild(self):
        if self._ampel.farbe == "rot":
            dateiname = "strassenampel.png"

        elif self._ampel.farbe == "rot-gelb":
            dateiname = "strassenampel_rot_gelb.png"

        elif self._ampel.farbe == "gelb":
            dateiname = "strassenampel_gelb.png"

        elif self._ampel.farbe == "gruen":
            dateiname = "strassenampel_gruen.png"
        
        else:
            raise Exception("Farbe ist undefiniert")

        self.img = Image.open(dateiname)
        self.img = self.img.resize((432, 267))
        self.bild = ImageTk.PhotoImage(self.img)
        Label(self, image=self.bild).place(x=0, y=0)  # type: ignore
        
    def _btn_exit_klick(self):
        self.quit()

ampel = AmpelElemente()
ampel.mainloop()

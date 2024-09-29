from tkinter import *


class weitereElemente(Tk):
    def __init__(self):
        super().__init__()

        self.title("GUI mit weiteren ELementen")
        self.geometry("350x400")

        # weitere Steuerelemente erzeugen
        self.erstellen_weiterer_elemente()

    def erstellen_weiterer_elemente(self):
        # Label mit dem Text Test
        self.lbl_test = Label(self, bg="silver", text="Test", width=8)
        self.lbl_test.grid(row=1, column=1, padx=5, pady=5)

        # Eingabefeld
        self.ent_test = Entry(self, bg="white", width=8)
        self.ent_test.grid(row=2, column=1, padx=5, pady=5)

        # Button zum Einfärben des Labels lbl_test
        self.btn_farbe = Button(
            self, text="Farbe", bg="gold", command=self.btn_farbe_klick)
        self.btn_farbe.grid(row=3, column=1, padx=5, pady=5)

        # Variable für den Checkbutton-Zustand (aktiv/deaktiv)
        self.var_chk_button = BooleanVar()
        # Checkbutton für "Farbe ändern"

        self.chk_farbe = Checkbutton(
            self, text="Farbe ändern", variable=self.var_chk_button)
        self.chk_farbe.grid(row=4, column=1, padx=5, pady=5)

        self.staedte_liste = ["Berlin", "Hamburg", "München"]
        # Variable für Radiobutton-Auswahl
        self.var_ausgewaehlte_stadt = StringVar(value="Berlin")

        # Radiobutton
        for s in self.staedte_liste:
            zeile = 5 + self.staedte_liste.index(s)
            (Radiobutton(self, text=s, value=s,variable=self.var_ausgewaehlte_stadt)).grid(
                row=zeile, column=1, padx=5, pady=5, sticky="w")

    def btn_farbe_klick(self):
        print(f"{self.var_chk_button.get()=}")
        print(f"{self.var_ausgewaehlte_stadt.get()=}")
        if self.var_chk_button.get():
            if self.btn_farbe["bg"] == "gold":
                self.lbl_test.config(bg="gold")
                self.btn_farbe.config(bg="silver")
            else:
                self.lbl_test.config(bg="silver")
                self.btn_farbe.config(bg="gold")

        self.lbl_test.config(text=self.var_ausgewaehlte_stadt.get())
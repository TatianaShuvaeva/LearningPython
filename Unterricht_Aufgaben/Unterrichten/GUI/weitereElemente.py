from tkinter import *

class GuiWeitereElemente(Tk):
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
        self.btn_farbe = Button(self, text="Farbe", bg="gold", command=self.btn_farbe_klick)
        self.btn_farbe.grid(row=3, column=1, padx=5, pady=5)

        # Variable für den Checkbutton-Zustand (aktiv/deaktiv)
        self.var_chk_button = BooleanVar()
        # Checkbutton für "Farbe ändern"
        self.chk_farbe = Checkbutton(self, text="Farbe ändern", variable=self.var_chk_button)
        self.chk_farbe.grid(row=4, column=1, padx=5, pady=5)

        self.staedte_liste = ["Berlin", "Hamburg", "München"]
        # Variable für Radiobutton-Auswahl
        self.var_ausgewaehlte_stadt = StringVar(value="Berlin")
        # Radiobutton
        for s in self.staedte_liste:
            zeile = 5 + self.staedte_liste.index(s)
            ((Radiobutton(self, text=s, value=s, variable=self.var_ausgewaehlte_stadt))
             .grid(row=zeile, column=1, padx=5, pady=5, sticky="w"))

        # Listbox
        self.lb = Listbox(self, height=4)
        self.lb.grid(row=1, column=2, padx=5, pady=5, rowspan=3)

        self.lb["selectmode"] = "extended"
        self.lb.insert("end", *self.staedte_liste)
        self.lb.bind("<<ListboxSelect>>", self.lb_auswahl)

        # Textbox
        self.tb = Text(self, bg="bisque", height=7, width=25)
        self.tb.grid(row=4, column=2, padx=5, pady=5, rowspan=3)

        # Scrollbar
        self.sb_tb = Scrollbar(self, command=self.tb.yview)
        self.sb_tb.grid(row=4, column=3, padx=5, pady=5, rowspan=3)
        self.tb.config(yscrollcommand=self.sb_tb.set)
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

    def lb_auswahl(self, event):
        auswahl = ", ".join(self.lb.get(i) for i in self.lb.curselection())
        print(f"{auswahl=}")
        self.tb.insert("end", auswahl+"\n")
       
    # def _berechnen_temperatur(self):
    #     pad_x = 120
    #     self.btn_c_nach_f = Button(self, text ="F", bg="lightpink", command=self.btn_c_nach_f_klick)
    #     self.btn_c_nach_f.grid(row=1, column=2, padx=pad_x, pady=5)
         
    #      # Eingabefeld
    #     self.ent_temperatur = Entry(self, bg="white", width=8)
    #     self.ent_temperatur.grid(row=2, column=2, padx=pad_x, pady=5)
        
    #     self.btn_f_nach_c = Button(self, text ="C", bg="lightgreen", command=self.btn_f_nach_c_klick)
    #     self.btn_f_nach_c.grid(row=3, column=2, padx=pad_x, pady=5)

    # def btn_c_nach_f_klick(self):
    #     value = float(self.ent_temperatur.get())
    #     calc = value* 9/5+32
    #     self.insert_temperatur(calc)
        
    # def insert_temperatur(self,calc:float):
    #     self.ent_temperatur.delete(0, 'end')
    #     self.ent_temperatur.insert(2, str(calc))
    
    # def btn_f_nach_c_klick(self):
    #     value = float(self.ent_temperatur.get())
    #     calc = (value-32) * 5/9
    #     self.insert_temperatur(calc)
    

    
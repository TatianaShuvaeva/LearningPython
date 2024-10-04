from tkinter import *
from tkinter import messagebox

class GuiWeitereElemente(Tk):
    def __init__(self):
        super().__init__()

        self.title("GUI mit weiteren ELementen")
        self.geometry("650x400")

        # weitere Steuerelemente erzeugen
        self.erstellen_weiterer_elemente()


    def erstellen_weiterer_elemente(self):
        # Nachrichten-Box (Message)
        text = ("Das GUI-Element Message wird verwendet, um einen Text anzuzeigen.\n"
                "Der Text soll aus mehreren Zeieln bestehen")
        self.mes_test = Message(self, bg="lightgreen", text=text, width=400)
        self.mes_test.grid(row=1, column=1, padx=5, pady=5)

        # Labelframe für Scale
        self.lf_sca = LabelFrame(self, text= "Test Scale", bg="beige")
        self.lf_sca.grid(row=2, column=1, padx=5, pady=5)
        # Schieberegler (Scale)
        self.sca_wert = Scale(self.lf_sca, orient=HORIZONTAL, from_=100, to=1000)
        self.sca_wert.grid(row=1, column=1, padx=5, pady=5)
        # Button zum "Ablesen"
        self.btn_ablesen = Button(self.lf_sca, text="Ablesen", command=self.btn_ablesen_klick)
        self.btn_ablesen.grid(row=2, column=1, padx=5, pady=5)
        # Label zum Anzeigen des abgelesenen Wertes
        self.lbl_sca_wert = Label(self.lf_sca, text= "??????")
        self.lbl_sca_wert.grid(row=3, column=1, padx=5, pady=5)

        # Labelframe für Spinbox
        self.lf_spb = LabelFrame(self, text= "Test Spinbox", bg="pink")
        self.lf_spb.grid(row=3, column=1, padx=5, pady=5)
        # Spinbox
        self.spb_wert = Spinbox(self.lf_spb, from_=100, to=1000)
        self.spb_wert.grid(row=1, column=1, padx=5, pady=5)
        # Button zum "Ablesen"
        self.btn_ablesen_spb = Button(self.lf_spb, text="Ablesen", command=self.btn_ablesen_spb_klick)
        self.btn_ablesen_spb.grid(row=2, column=1, padx=5, pady=5)
        # Label zum Anzeigen des abgelesenen Wertes
        self.lbl_spb_wert = Label(self.lf_spb, text= "??????")
        self.lbl_spb_wert.grid(row=3, column=1, padx=5, pady=5)

        # Labelframe Messagebox
        self.lf_msg = LabelFrame(self, text= "Test Messagebox", bg="azure")
        self.lf_msg.grid(row=4, column=1, padx=5, pady=5)

        # Button ok cancel
        self.btn_ok_cancel = Button(self.lf_msg, text="ok_cancel", bg="gold", command=self.btn_ok_cancel_klick)
        self.btn_ok_cancel.grid(row=1, column=1, padx=5, pady=5)
        # Button ###
        self.btn_b2 = Button(self.lf_msg, text="#####", bg="gold")
        self.btn_b2.grid(row=1, column=2, padx=5, pady=5)


    def btn_ablesen_klick(self):
        print( self.sca_wert.get() )
        self.lbl_sca_wert.config(text=self.sca_wert.get())

    def btn_ablesen_spb_klick(self):
        print( self.spb_wert.get() )
        self.lbl_spb_wert.config(text=self.spb_wert.get())

    def btn_ok_cancel_klick(self):
        ergebnis = messagebox.askokcancel("Beenden", "Programm beenden?")
        if ergebnis:
            print("ok")
        else:
            print("cancel")
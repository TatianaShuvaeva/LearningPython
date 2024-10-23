import tkinter as tk
from tkinter import ttk, messagebox, Menu, simpledialog, filedialog, colorchooser

class TkDialoge_App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TK Dialoge")
        self.geometry('400x400')

        # Benutzereingabe
        self.btn_input = ttk.Button(self, text="Texteingabe", command=self.ask_for_input)
        self.btn_input.pack(pady=10)

        # Datei-/Verzeichnis-Dialog
        self.btn_datei = ttk.Button(self, text="Dateiauswahl öffnen", command=self.open_file_dialog)
        self.btn_datei.pack(pady=10)

        # Farb-Dialog
        self.btn_farbe = ttk.Button(self, text="Farbauswahl öffnen", command=self.farbauswahl_dialog)
        self.btn_farbe.pack(pady=10)

    def ask_for_input(self):
        user_input = simpledialog.askstring("Eingabe", "Bitte eine Float-Zahl eingeben")
        if user_input:
            print(f"Benutzereingabe: {user_input}")

    def open_file_dialog(self):
        dateipfad = (filedialog.askopenfilename(title="Dateiauswahl",
                                               filetypes=[("Pythondateien", "*.py"),
                                                          ("Textdateien", "*.txt"),
                                                          ("alle Dateien", "*.*")]))
        print(f"ausgewählte Datei: {dateipfad}")

    def farbauswahl_dialog(self):
        farbe = colorchooser.askcolor(title="Farbauswahl")
        print(f"Rückgabe: {farbe}")
        if farbe[0] is not None:
            print(f"ausgewählte Farbe als RBG_Farbwert: {farbe[0]}")
            print(f"ausgewählte Farbe als hex-Farbwert: {farbe[1]}")
        else:
            print(f"es wurde keine Farbe ausgewählt {farbe}")
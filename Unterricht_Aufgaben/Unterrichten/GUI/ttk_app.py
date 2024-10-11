import tkinter as tk
from tkinter import ttk, messagebox, Menu
import random

class Ttk_App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TTK Beispiel")
        self.geometry('800x800')

        # Style für ttk-Widgets definieren
        self.style = ttk.Style()
        self.configure_styles()

        # Menüleiste erstellen
        self.create_menubar()

        # Hauptlayout mit PanedWindow und Frames
        self.main_frame = ttk.Frame(self, padding=20, style='TFrame')
        self.main_frame.pack(fill='both', expand=True)

        # PanedWindow für mehrspaltiges Layout
        self.panedwindow = ttk.PanedWindow(self.main_frame, orient=tk.HORIZONTAL)
        self.left_frame = ttk.Frame(self.panedwindow, padding=10, style='TFrame')
        self.right_frame = ttk.Frame(self.panedwindow, padding=10, style='TFrame')

        self.panedwindow.add(self.left_frame, weight=1)
        self.panedwindow.add(self.right_frame, weight=1)
        self.panedwindow.pack(fill=tk.BOTH, expand=True)

        # Widgets erstellen und in das Layout einfügen
        self.create_widgets()

    def configure_styles(self):
        """Definiere Stile für alle ttk-Widgets."""
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 14), foreground='black')
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TEntry', foreground='black', font=('Helvetica', 12), padding=5)
        self.style.configure('TCheckbutton', font=('Helvetica', 12))
        self.style.configure('TRadiobutton', font=('Helvetica', 12))
        self.style.configure('TCombobox', font=('Helvetica', 12))
        self.style.configure('Horizontal.TScale', font=('Helvetica', 12))

    def create_menubar(self):
        """Erstellt die Menüleiste."""
        menubar = Menu(self)
        self.config(menu=menubar)

        # Datei Menü
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Datei", menu=file_menu)
        file_menu.add_command(label="Neu", command=self.new_file)
        file_menu.add_command(label="Öffnen", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Beenden", command=self.quit)

        # Hilfe Menü
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Hilfe", menu=help_menu)
        help_menu.add_command(label="Über", command=self.about)

    def create_widgets(self):
        """Erstellt die Widgets und fügt sie in das Layout ein."""
        # Linkes Panel mit Eingabefeldern
        ttk.Label(self.left_frame, text="TTK Label Beispiel", style='TLabel').grid(row=0, column=0, pady=10, sticky='w')
        self.entry = ttk.Entry(self.left_frame, width=20, style='TEntry')
        self.entry.grid(row=1, column=0, pady=10, sticky='w')

        self.check_var = tk.IntVar()
        self.checkbutton = ttk.Checkbutton(self.left_frame, text="Checkbutton Beispiel", variable=self.check_var, style='TCheckbutton')
        self.checkbutton.grid(row=2, column=0, pady=10, sticky='w')

        self.radio_var = tk.IntVar()
        self.radiobutton1 = ttk.Radiobutton(self.left_frame, text="Option 1", value=1, variable=self.radio_var, style='TRadiobutton')
        self.radiobutton2 = ttk.Radiobutton(self.left_frame, text="Option 2", value=2, variable=self.radio_var, style='TRadiobutton')
        self.radiobutton1.grid(row=3, column=0, pady=5, sticky='w')
        self.radiobutton2.grid(row=4, column=0, pady=5, sticky='w')

        self.combobox = ttk.Combobox(self.left_frame, values=["Option 1", "Option 2", "Option 3"], style='TCombobox')
        self.combobox.grid(row=5, column=0, pady=10, sticky='w')

        self.spinbox = ttk.Spinbox(self.left_frame, from_=0, to=10, style='TSpinbox')
        self.spinbox.grid(row=6, column=0, pady=10, sticky='w')

        self.scale = ttk.Scale(self.left_frame, from_=0, to=100, orient='horizontal', style='Horizontal.TScale')
        self.scale.grid(row=7, column=0, pady=10, sticky='w')

        self.text = tk.Text(self.left_frame, height=5, width=30)
        self.text.grid(row=8, column=0, pady=10, sticky='w')

        # Button zum Ablesen der Werte
        self.button_read = ttk.Button(self.left_frame, text="Werte ablesen", style='TButton', command=self.read_values)
        self.button_read.grid(row=9, column=0, pady=10)

        # Rechtes Panel mit Treeview, Progressbar und Canvas
        self.lbf_tv = ttk.LabelFrame(self.right_frame, text="Treeview Test")
        self.lbf_tv.grid(row=0, column=0, padx=5, pady=5)

        self.tree = ttk.Treeview(self.lbf_tv, columns=('col1', 'col2'), show='headings')
        self.tree.heading('col1', text='Name')
        self.tree.heading('col2', text='Alter')
        self.tree.insert('', 'end', values=('Max', 25))
        self.tree.insert('', 'end', values=('Anna', 30))
        self.tree.grid(row=0, column=0, pady=10)

        self.lbf_pb = ttk.LabelFrame(self.right_frame, text="Progressbar Test")
        self.lbf_pb.grid(row=1, column=0, padx=5, pady=5)
        self.progressbar = ttk.Progressbar(self.lbf_pb, orient='horizontal', length=200, mode='determinate')
        self.progressbar.grid(row=1, column=0, pady=10)
        self.progressbar['value'] = 50  # Beispielwert

        # Canvas für Zeichnungen
        self.lbf_cv = ttk.LabelFrame(self.right_frame, text="Canvas Test")
        self.lbf_cv.grid(row=2, column=0, padx=5, pady=5)
        self.canvas = tk.Canvas(self.lbf_cv, width=200, height=200, bg='white')
        self.canvas.grid(row=1, column=1, pady=10)
        self.canvas.create_oval(50, 20, 150, 120, fill="blue", tags="kreis")
        # Window - hier ein Button
        self.btn_kreis_farbe = ttk.Button(None, text="Farbe ändern", command=self.btn_kreis_farbe_klick)
        self.canvas.create_window(100, 160, window=self.btn_kreis_farbe)

    def btn_kreis_farbe_klick(self):
        colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        self.canvas.itemconfig("kreis", fill=random.choice(colors))

    def read_values(self):
        """Liest die Werte der verschiedenen Widgets aus und zeigt sie an."""
        entry_value = self.entry.get()
        check_value = "aktiviert" if self.check_var.get() == 1 else "deaktiviert"
        radio_value = f"Option {self.radio_var.get()}" if self.radio_var.get() != 0 else "Keine Option gewählt"
        combo_value = self.combobox.get() if self.combobox.get() != '' else "Keine Auswahl"
        spinbox_value = self.spinbox.get()
        scale_value = int(self.scale.get())
        text_value = self.text.get("1.0", tk.END).strip()

        # Zeige die Werte in einer Messagebox an
        messagebox.showinfo("Abgelesene Werte",
                            f"Entry: {entry_value}\n"
                            f"Checkbutton: {check_value}\n"
                            f"Radiobutton: {radio_value}\n"
                            f"Combobox: {combo_value}\n"
                            f"Spinbox: {spinbox_value}\n"
                            f"Scale: {scale_value}\n"
                            f"Text: {text_value}")

    def new_file(self):
        """Aktion für den Menüpunkt 'Neu'."""
        messagebox.showinfo("Neu", "Neue Datei erstellen")

    def open_file(self):
        """Aktion für den Menüpunkt 'Öffnen'."""
        messagebox.showinfo("Öffnen", "Datei öffnen")

    def about(self):
        """Zeigt Informationen zum Programm an."""
        messagebox.showinfo("Über", "Erweiterte GUI mit Menüleiste und Canvas")
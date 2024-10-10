from tkinter import *
from tkinter import messagebox

class GUIMitKreis(Tk):
    
    def __init__(self):
        super().__init__()

        self.title("GUI mit weiteren ELementen")
        self.geometry("650x700")

        self.ausgewaehlter_kreis = NONE
        self.last_x = 0
        self.last_y = 0

        # Steuerelemente erzeugen
        self.create_widgets()

    def create_widgets(self):
        self.lf_cv = LabelFrame(self, bg="lightblue", text="Canvas Test")
        self.lf_cv.grid(row=1, column=1, padx=5, pady=5)
        self.cv = Canvas(self.lf_cv, width=500, height=500, bg="beige")
        self.cv.grid(row=1, column=1, padx=5, pady=5)

        # Kreis zeichnen
        self.cv.create_oval(200, 280, 350, 430, fill="orange", width=5)
        # Ellipse zeichnen
        self.cv.create_oval(50, 180, 150, 200, fill="blue", width=5)

        # Linie zeichnen
        self.cv.create_line(20, 280, 40, 430, fill="green", width=5)

        # Vieleck (Polygon) zeichnen
        self.cv.create_polygon(320, 20, 540, 130, 380, 350, fill="yellow", outline="black", width=5)

        # Bild einfügen
        self.cv_img = PhotoImage(file="kleinerPrinz.jpg")
        self.cv.create_image(10, 10, image=self.cv_img, anchor="nw", tags="pic1")
        # Event-Binding
        self.cv.tag_bind("pic1", "<Button-1>", lambda event, tag="pic1": self.start_move(event, tag))
        self.cv.tag_bind("pic1", "<B1-Motion>", lambda event, tag="pic1": self.item_move(event, tag))

        # im Canvas einen Button defnieren
        self.btn_cv_farbe_tauschen = Button(None, text="Farbe tauschen", command=self.btn_cv_farbe_tauschen_klick)
        self.cv.create_window(200, 275, window=self.btn_cv_farbe_tauschen)

        self.btn_cv_size = Button(self.lf_cv, text="Canvas vergrößern", bg="khaki", command=self.btn_cv_size_klick)
        self.btn_cv_size.grid(row=2, column=1, padx=5, pady=5)

        self.btn_kreis_erstellen = Button(self.lf_cv, text="Kreis zeichnen", bg="khaki", command=self.btn_kreis_zeichnen_klick)
        self.btn_kreis_erstellen.grid(row=3, column=1, padx=5, pady=5)


    def btn_cv_size_klick(self):
        new_width = self.cv.winfo_width() * 1.1
        new_height = self.cv.winfo_height() * 1.1
        self.cv.config(width=new_width, height=new_height)

    def btn_kreis_zeichnen_klick(self):
        # Kreise zeichnen
        self.cv.create_oval(20, 20, 100, 100, fill="blue", width=5, tags="kreis1")
        # Event-Binding
        self.cv.tag_bind("kreis1", "<Button-1>", lambda event, tag="kreis1": self.start_move(event, tag))
        self.cv.tag_bind("kreis1", "<B1-Motion>", lambda event, tag="kreis1": self.item_move(event, tag))

        self.cv.create_oval(120, 120, 180, 180, fill="orange", width=5, tags="kreis2")
        self.cv.tag_bind("kreis2", "<Button-1>", lambda event, tag="kreis2": self.start_move(event, tag))
        self.cv.tag_bind("kreis2", "<B1-Motion>", lambda event, tag="kreis2": self.item_move(event, tag))

    def btn_cv_farbe_tauschen_klick(self):
        farbe1 = self.cv.itemcget("kreis1", "fill")
        farbe2 = self.cv.itemcget("kreis2", "fill")

        self.cv.itemconfig("kreis1", fill=farbe2)
        self.cv.itemconfig("kreis2", fill=farbe1)

    def start_move(self, event, tag):
        # Position des Elementes merken
        self.ausgewaehlter_kreis = tag
        self.last_x = event.x
        self.last_y = event.y

    def item_move(self, event, tag):
        dx = event.x - self.last_x
        dy = event.y - self.last_y
        self.cv.move(tag, dx, dy)
        # aktualisiere die letzte Mausposition
        self.last_x = event.x
        self.last_y = event.y
from tkinter import *
from operatorüberladung_bruche import Bruch
from PIL import Image, ImageTk

def eingabebruch(eingabe):
    zahl = eingabe.split("/")
    zähler = int(zahl [0])
    nenner = int(zahl [1])
    return Bruch(zähler, nenner)

def btnplusklick():
    bruch1 = eingabebruch(entbruch1.get())
    bruch2 = eingabebruch(entbruch2.get())
    ergebnis = bruch1 + bruch2
    lblergebnis.config(text = str(ergebnis))

def btnminusklick():
    bruch1 = eingabebruch(entbruch1.get())
    bruch2 = eingabebruch(entbruch2.get())
    ergebnis = bruch1 - bruch2
    lblergebnis.config(text = str(ergebnis))

def btnmalklick():
    bruch1 = eingabebruch(entbruch1.get())
    bruch2 = eingabebruch(entbruch2.get())
    ergebnis = bruch1 * bruch2
    lblergebnis.config(text = str(ergebnis))

def btngeteiltklick():
    bruch1 = eingabebruch(entbruch1.get())
    bruch2 = eingabebruch(entbruch2.get())
    ergebnis = bruch1 / bruch2
    lblergebnis.config(text = str(ergebnis))

# Fenster definieren

gui = Tk()
gui.title("Rechner")
gui.geometry("240x200")

# Definition der Elemente


img = Image.open("hintergrund.jpg")
img = img.resize((240, 200))
bild = ImageTk.PhotoImage(img)
Label(gui, image=bild).place(x = 0, y = 0)

lblbruch1 = Label(gui, text = "Bruch 1", background = "#AB82FF")
lblbruch1.grid(row = 0, column = 0, padx = 5, pady = 5)

entbruch1 = Entry(gui, width = 8)
entbruch1.grid(row = 1, column = 0, padx = 5, pady = 5)

# Bruch 2

lblbruch2 = Label(gui, text = "Bruch 2", background = "#AB82FF")
lblbruch2.grid(row = 0, column = 4, padx = 5, pady = 5)

entbruch2 = Entry(gui, width = 8)
entbruch2.grid(row = 1, column = 4, padx = 5, pady = 5)

# Buttons definieren

img = Image.open("plus_button.jpg")
img = img.resize((20, 20))
plusbild = ImageTk.PhotoImage(img)

btnplus = Button(gui, image = plusbild, command = btnplusklick, background = "#E6E6FA", activebackground = "#AB82FF")
btnplus.grid(row = 2, column = 0, padx = 5, pady = 5)

btnminus = Button(gui, text = "-", command = btnminusklick, background = "#E6E6FA", activebackground = "#AB82FF")
btnminus.grid(row = 2, column = 1, padx = 5, pady = 5)

btnmal = Button(gui, text = "*", command = btnmalklick, background = "#E6E6FA", activebackground = "#AB82FF")
btnmal.grid(row = 2, column = 3, padx = 5, pady = 5)

btngeteilt = Button(gui, text = ":", command = btngeteiltklick, background = "#E6E6FA", activebackground = "#AB82FF")
btngeteilt.grid(row = 2, column = 4,  padx = 5, pady = 5)

# Ausgabe & Ergebnis

lbltextergebnis = Label(gui, text = "Ergebnis", background = "#AB82FF")
lbltextergebnis.grid(row = 3, column = 2, padx = 5, pady = 5)

lblergebnis = Label(gui, text = "?")
lblergebnis.grid(row = 4, column = 2, padx = 5, pady = 5)

# Layout definieren

# Interaktivität

gui.mainloop()
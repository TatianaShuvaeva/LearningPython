from tkinter import *
from operatorüberladung_bruche import Bruch


def eingeben_bruch(eingabe):
    zahl = eingabe.split("/")
    zahler = int(zahl[0])
    nenner = int(zahl[1])
    return Bruch(zahler, nenner)


def btnplusklick():
    bruch1 = eingeben_bruch(entbruch1.get())

    bruch2 = eingeben_bruch(entbruch2.get())

    # lblergebnis.config(text=str(ergebnis))
    ergebnis = bruch1 + bruch2
    lblergebnis.config(text=str(ergebnis))


def btnminusklick():
    bruch1 = eingeben_bruch(entbruch1.get())

    bruch2 = eingeben_bruch(entbruch2.get())

    ergebnis = bruch1 - bruch2
    lblergebnis.config(text=str(ergebnis))


def btnmalklick():
    bruch1 = eingeben_bruch(entbruch1.get())

    bruch2 = eingeben_bruch(entbruch2.get())

    ergebnis = bruch1 * bruch2
    lblergebnis.config(text=str(ergebnis))


def btngeteiltklick():
    bruch1 = eingeben_bruch(entbruch1.get())

    bruch2 = eingeben_bruch(entbruch2.get())

    ergebnis = bruch1/bruch2
    lblergebnis.config(text=str(ergebnis))


# Fenster definieren
rechner = Tk()
rechner.title("Rechner")
rechner.geometry("250x300")

# Definition der Elemente


lblbbuch1 = Label(rechner, text="Bruch 1", bg="lightpink")
lblbbuch1.grid(row=0, column=0, padx=5, pady=5)
entbruch1 = Entry(rechner, width=8)
entbruch1.grid(row=1, column=0, padx=5, pady=5)


lblbbuch2 = Label(rechner, text="Bruch 2", bg="lightpink")
lblbbuch2.grid(row=0, column=4, padx=5, pady=5)
entbruch2 = Entry(rechner, width=8)
entbruch2.grid(row=1, column=4, padx=5, pady=5)


btnplus = Button(rechner, text="+", command=btnplusklick)
btnplus.grid(row=2, column=0, padx=5, pady=5)

btnminus = Button(rechner, text="-", command=btnminusklick)
btnminus.grid(row=2, column=1, padx=5, pady=5)

btnmal = Button(rechner, text="*", command=btnmalklick)
btnmal.grid(row=2, column=3, padx=5, pady=5)

btngeteilt = Button(rechner, text="/", command=btngeteiltklick)
btngeteilt.grid(row=2, column=4, padx=5, pady=5)


lbltextergebnis = Label(rechner, text="Ergebnis", bg="lightgreen")
lbltextergebnis.grid(row=4, column=2, padx=5, pady=5)
lblergebnis = Label(rechner, text="?")
lblergebnis.grid(row=5, column=2, padx=5, pady=5)

# label2 = Label(master = rechner, text = "Zweites Anzeigefeld", bg="red")
# label2.pack(side="left")
# button = Button(rechner, text = "Save", bg ="yellow", width = 10)
# button.pack(side ="right")
# Layout
# Layout
# Interaktivität
rechner.mainloop()

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
    lblergebnis.config(text = str(ergebnis))
    

def btnminusklick():
    bruch1 = eingeben_bruch(entbruch1.get())
     
    bruch2 = eingeben_bruch(entbruch2.get())
   
    ergebnis = bruch1 - bruch2
    lblergebnis.config(text = str(ergebnis))
    
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
rechner.geometry("200x300")

# Definition der Elemente
frmeingabe = Frame(rechner)
frmeingabe.pack(pady=10)

frmbruch1 = Frame(frmeingabe, bg = "lightpink", bd=2)
frmbruch1.pack(padx=5, pady=5, side="left")

lblbbuch1 = Label(frmbruch1, text="Bruch 1")
lblbbuch1.pack(padx=5, pady=5)
entbruch1 = Entry(frmbruch1, width=8)
entbruch1.pack(padx=5, pady=5)

frmbruch2 = Frame(frmeingabe, bg="lightpink")
frmbruch2.pack(padx=5, pady=5, side="right")
lblbbuch2 = Label(frmbruch2, text="Bruch 2")
lblbbuch2.pack(padx=5, pady=5)
entbruch2 = Entry(frmbruch2, width=8)
entbruch2.pack(padx=5, pady=5)
frmberechnen = Frame(rechner, bg="yellow")
frmberechnen.pack()
btnplus = Button(frmberechnen, text="+", command=btnplusklick)
btnplus.pack(side="left", padx=5, pady=5)

btnminus = Button(frmberechnen, text="-", command=btnminusklick)
btnminus.pack(side="left", padx=5, pady=5)

btnmal = Button(frmberechnen, text="*", command=btnmalklick)
btnmal.pack(side="left", padx=5, pady=5)

btngeteilt = Button(frmberechnen, text="/", command=btngeteiltklick)
btngeteilt.pack(side="left", padx=5, pady=5)

frmausgabe = Frame(rechner, bg="lightgreen")
frmausgabe.pack(padx=5, pady=5)
lbltextergebnis = Label(frmausgabe, text="Ergebnis")
lbltextergebnis.pack(padx=5, pady=5)
lblergebnis = Label(frmausgabe, text="?")
lblergebnis.pack(padx=5, pady=5)

# label2 = Label(master = rechner, text = "Zweites Anzeigefeld", bg="red")
# label2.pack(side="left")
# button = Button(rechner, text = "Save", bg ="yellow", width = 10)
# button.pack(side ="right")
# Layout
# Layout
# Interaktivität
rechner.mainloop()

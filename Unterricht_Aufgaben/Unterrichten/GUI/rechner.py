from tkinter import *
# Fenster definieren
rechner = Tk()
rechner.title("Rechner")
rechner.geometry("600x600")

# Definition der Elemente
label1 = Label(master = rechner, text = "Erstes Anzeigefeld", bg="green")
label1.pack(side="left")
entry = Entry(master = rechner)
entry.pack(side="left")
label2 = Label(master = rechner, text = "Zweites Anzeigefeld", bg="red")
label2.pack(side="left")
button = Button(rechner, text = "Save", bg ="yellow", width = 10)
button.pack(side ="right")
#Layout
# Layout 
# Interaktivität
rechner.mainloop() 
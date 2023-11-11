import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
from math import pi


def hitung_luas():
     r = float(txtjari.get())
     T = float(txttinggi.get())
     s = float(txtselimut.get())


     L = round(pi * r * s + pi * r **2)

     txtLuas.delete(0,END)
     txtLuas.insert(END,L)

def hitung_volume():
     r = float(txtjari.get())
     T = float(txttinggi.get())
     s = float(txtselimut.get())



     v = round((1/3) * pi * r**2 * T)

     txtVolume.delete(0,END)
     txtVolume.insert(END,v)


def hitung():
    hitung_luas()
    hitung_volume()

# Create
app = tk.Tk()

# Judul
app.title("Kalkulator Luas dan Volume Kerucut")

# Windows
frame = Frame(app)
frame.pack (padx=20, pady=20)

# Label jari-jari
jari = Label(frame, text="jari-jari :")
jari.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox jari-jari
txtjari = Entry(frame)
txtjari.grid(row=0, column=1)

# Label selimut
selimut = Label(frame, text="Luas selimut :")
selimut.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox selimut
txtselimut = Entry(frame)
txtselimut.grid(row=1, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas= Label(frame, text="Luas:" )
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1)

# Output Volume
volume= Label(frame, text="Volume:" )
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)
#  Textbox Volume 
txtVolume = Entry(frame)
txtVolume.grid(row=5, column=1)

app.mainloop()
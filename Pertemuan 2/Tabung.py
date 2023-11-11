import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
from math import pi

def hitung_luasselimut():
    r = float(txtjari.get())
    t = float(txttinggi.get())


    LS = round(2 * pi * r * t)

    txtluasselimut.delete(0,END)
    txtluasselimut.insert(END,LS)

def hitung_luaspermukaan():
    r = float(txtjari.get())
    t = float(txttinggi.get())

    LP = round(2 * pi * r * t + 2 * pi * r **2)

    txtluaspermukaan.delete(0,END)
    txtluaspermukaan.insert(END,LP)

def hitung_volume():
    r = float(txtjari.get())
    t = float(txttinggi.get())

    v = round(pi * r **2 * t)

    txtVolume.delete(0,END)
    txtVolume.insert(END,v)



def hitung():
    hitung_luasselimut()
    hitung_luaspermukaan()
    hitung_volume()

# Create
app = tk.Tk()

# Judul
app.title("Kalkulator Luas dan Volume Tabung")


# Windows
frame = Frame(app)
frame.pack (padx=50, pady=50)


# Label jari-jari
jari = Label(frame, text="jari-jari :")
jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Lebar
txtjari = Entry(frame)
txtjari.grid(row=1, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas selimut
luasselimut= Label(frame, text="Luas selimut :" )
luasselimut.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas selimut
txtluasselimut = Entry(frame)
txtluasselimut.grid(row=4, column=1)

# Output Label Luas Permukaan
luaspermukaan= Label(frame, text="Luas permukaan :" )
luaspermukaan.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Permukaan
txtluaspermukaan = Entry(frame)
txtluaspermukaan.grid(row=5, column=1)

# Output Volume
volume= Label(frame, text="Volume:" )
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)
#  Textbox Volume 
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1)

app.mainloop()
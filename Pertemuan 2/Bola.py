import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
from math import pi

def hitung_luasbola():
    r = float(txtjari.get())

    LB = round(4 * pi * r**2)

    txtluasbola.delete(0,END)
    txtluasbola.insert(END,LB)

def hitung_volume():
    r = float(txtjari.get())

    v = round(4/3 * pi * r**3)

    txtVolume.delete(0,END)
    txtVolume.insert(END,v)



def hitung():
    hitung_luasbola()
    hitung_volume()

# Create
app = tk.Tk()

# Judul
app.title("Kalkulator Luas dan Volume Bola")


# Windows
frame = Frame(app)
frame.pack (padx=50, pady=50)


# Label jari-jari
jari = Label(frame, text="jari-jari :")
jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Lebar
txtjari = Entry(frame)
txtjari.grid(row=1, column=1)


# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)


# Output Label Luas Bola
luasbola= Label(frame, text="Luas Bola :" )
luasbola.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Bola
txtluasbola = Entry(frame)
txtluasbola.grid(row=5, column=1)

# Output Volume
volume= Label(frame, text="Volume:" )
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)
#  Textbox Volume 
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1)

app.mainloop()
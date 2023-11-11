import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
from math import pi

def hitung_luas():
    a = float(txtalas.get())
    t = float(txttinggi.get())
    s = float(txtsisi.get())
    L = round((a*t/2)*4 + (s*s))

    txtluas.delete(0,END)
    txtluas.insert(END,L)

def hitung_volume():
    a = float(txtalas.get())
    t = float(txttinggi.get())
    s = float(txtsisi.get())
    v = round(1/3*(s*s)*t)

    txtVolume.delete(0,END)
    txtVolume.insert(END,v)



def hitung():
    hitung_luas()
    hitung_volume()

# Create
app = tk.Tk()

# Judul
app.title("Kalkulator Luas dan Volume limas segiempat")


# Windows
frame = Frame(app)
frame.pack (padx=60, pady=60)


# Label alas
alas = Label(frame, text="alas :")
alas.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox alas
txtalas = Entry(frame)
txtalas.grid(row=0, column=1)

# Label tinggi
tinggi = Label(frame, text="tinggi :")
tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox lebar
txttinggi = Entry(frame)
txttinggi.grid(row=1, column=1)

# Label sisi
sisi = Label(frame, text="sisi :")
sisi.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox tinggi
txtsisi = Entry(frame)
txtsisi.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas= Label(frame, text="Luas :" )
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas
txtluas = Entry(frame)
txtluas.grid(row=4, column=1)

# Output Volume
volume= Label(frame, text="Volume:" )
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)
#  Textbox Volume 
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1)

app.mainloop()
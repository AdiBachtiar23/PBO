import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
from math import pi

def hitung_luas():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())
    t = float(txttinggi.get())
    L = round((2*p*l)+(2*p*l)+(2*l*t))

    txtluas.delete(0,END)
    txtluas.insert(END,L)

def hitung_volume():
    p = float(txtpanjang.get())
    l = float(txtluas.get())
    t = float(txttinggi.get())
    v = round(p*l*t)

    txtVolume.delete(0,END)
    txtVolume.insert(END,v)



def hitung():
    hitung_luas()
    hitung_volume()

# Create
app = tk.Tk()

# Judul
app.title("Kalkulator Luas dan Volume balok")


# Windows
frame = Frame(app)
frame.pack (padx=60, pady=60)


# Label panjang
panjang = Label(frame, text="panjang :")
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=0, column=1)

# Label lebar
lebar = Label(frame, text="lebar :")
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox lebar
txtlebar = Entry(frame)
txtlebar.grid(row=1, column=1)

# Label tinggi
tinggi = Label(frame, text="tinggi :")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

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
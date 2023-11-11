import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
from math import pi

def hitung_luas():
    s = float(txtsisi.get())
    L = round(6*s*s)

    txtluas.delete(0,END)
    txtluas.insert(END,L)

def hitung_volume():
    s = float(txtsisi.get())
    v = round(s*s*s)

    txtVolume.delete(0,END)
    txtVolume.insert(END,v)



def hitung():
    hitung_luas()
    hitung_volume()

# Create
app = tk.Tk()

# Judul
app.title("Kalkulator Luas dan Volume kubus")


# Windows
frame = Frame(app)
frame.pack (padx=60, pady=60)


# Label sisi
sisi = Label(frame, text="sisi :")
sisi.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox sisi
txtsisi = Entry(frame)
txtsisi.grid(row=0, column=1)

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
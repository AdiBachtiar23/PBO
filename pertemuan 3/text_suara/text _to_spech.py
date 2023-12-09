import tkinter as tk
from tkinter import Label, Entry, Button, filedialog
from gtts import gTTS
import os
import pygame

def convert_to_speech():
    text = entry_text.get()
    language = 'id'  # Bahasa sesuai kebutuhan

    try:
        # Buat objek gTTS
        tts = gTTS(text=text, lang=language, slow=False)

        # Hapus file audio lama jika ada
        if os.path.exists("output.mp3"):
            os.remove("output.mp3")

        # Simpan file audio
        tts.save("output.mp3")

        # Putar file audio yang telah disimpan
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

    except Exception as e:
        print(f"Error: {e}")

# Buat jendela utama
root = tk.Tk()
root.title("Konversi Teks-menjadi-Suara")

# Mendapatkan ukuran layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Mendapatkan ukuran window
window_width = 300
window_height = 150

# Menghitung posisi tengah window
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Mengatur posisi window
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Buat widget
label_instruction = Label(root, text="Masukkan teks untuk dikonversi:")
entry_text = Entry(root, width=50)
button_convert = Button(root, text="Konversi ke Suara", command=convert_to_speech)

# Tempatkan widget pada jendela
label_instruction.pack(pady=10)
entry_text.pack(pady=10)
button_convert.pack(pady=10)

# Mulai perulangan acara GUI
root.mainloop()

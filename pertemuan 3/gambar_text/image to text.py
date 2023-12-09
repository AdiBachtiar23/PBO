import tkinter as tk
from tkinter import filedialog
import PIL.Image, PIL.ImageTk
import pytesseract
import os

# Set the path to the Tesseract executable (replace with your actual path)
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

def image_to_text(image_path):
    try:
        img = PIL.Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error: {e}"

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png;.jpg;*.jpeg")])
    if file_path:
        display_image(file_path)
        result_text = image_to_text(file_path)
        result_var.set(result_text)

def display_image(image_path):
    try:
        img = PIL.Image.open(image_path)
        img.thumbnail((300, 300))  # Resize the image for display
        img = PIL.ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img  # Keep a reference to the image to prevent garbage collection
    except Exception as e:
        result_var.set(f"Error: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Image to Text Converter")

# Mendapatkan ukuran layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Mendapatkan ukuran window
window_width = 300
window_height = 150

# Menghitung posisi tengah window
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Create and configure widgets
browse_button = tk.Button(root, text="Browse Image", command=browse_image)
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, wraplength=400, justify='left')
image_label = tk.Label(root)

# Place widgets in the window
browse_button.pack(pady=10)
image_label.pack(pady=10)
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
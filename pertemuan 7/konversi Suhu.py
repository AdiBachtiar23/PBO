import tkinter as tk

def convert_temperature():
    try:
        # Ambil nilai dari inputan pengguna
        input_temperature = float(entry_temperature.get())

        # Ambil jenis suhu yang dipilih
        input_scale = combo_from.get()
        output_scale = combo_to.get()

        # Lakukan konversi suhu
        if input_scale == "Celsius" and output_scale == "Fahrenheit":
            result = (input_temperature * 9/5) + 32
        elif input_scale == "Celsius" and output_scale == "Kelvin":
            result = input_temperature + 273.15
        elif input_scale == "Fahrenheit" and output_scale == "Celsius":
            result = (input_temperature - 32) * 5/9
        elif input_scale == "Fahrenheit" and output_scale == "Kelvin":
            result = (input_temperature - 32) * 5/9 + 273.15
        elif input_scale == "Kelvin" and output_scale == "Celsius":
            result = input_temperature - 273.15
        elif input_scale == "Kelvin" and output_scale == "Fahrenheit":
            result = (input_temperature - 273.15) * 9/5 + 32
        else:
            result = input_temperature  # Jika jenis suhu sama, hasilnya tetap

        # Update label dengan hasil konversi
        label_result.config(text=f"Result: {result:.2f} {output_scale}")

    except ValueError:
        # Tangani jika pengguna memasukkan sesuatu yang bukan angka
        label_result.config(text="Please enter a valid temperature")

# Buat instance dari Tkinter
root = tk.Tk()
root.title("Temperature Converter")
root.config(bg="black")
root.geometry("350x300")
root.resizable(width=False,height=False)

# Buat label untuk input suhu
label_temperature = tk.Label(root, text="Enter Temperature:")
label_temperature.pack(pady=10)

# Buat entry untuk memasukkan suhu
entry_temperature = tk.Entry(root)
entry_temperature.pack(pady=10)

# Buat label untuk memilih jenis suhu dari
label_from = tk.Label(root, text="From:")
label_from.pack()

# Buat dropdown untuk memilih jenis suhu dari
options = ["Celsius", "Fahrenheit", "Kelvin"]
combo_from = tk.StringVar()
combo_from.set(options[0])  # Set default value
dropdown_from = tk.OptionMenu(root, combo_from, *options)
dropdown_from.pack(pady=10)

# Buat label untuk memilih jenis suhu ke
label_to = tk.Label(root, text="To:")
label_to.pack()

# Buat dropdown untuk memilih jenis suhu ke
combo_to = tk.StringVar()
combo_to.set(options[1])  # Set default value
dropdown_to = tk.OptionMenu(root, combo_to, *options)
dropdown_to.pack(pady=10)

# Buat tombol konversi suhu
button_convert = tk.Button(root, text="Convert", command=convert_temperature)
button_convert.pack(pady=20)

# Buat label untuk menampilkan hasil konversi
label_result = tk.Label(root, text="Result:")
label_result.pack()

# Jalankan aplikasi Tkinter
root.mainloop()
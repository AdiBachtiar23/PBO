import math

print("program menghitung luas dan volume bola")
"""

programmer : Adi Bachtiar
Nim : 220511173
pertemuan : 1
tanggal : 22 Oktober 2023
"""

# nilai

r = float(input("masukan nilai : "))


# rumus
luas = 4*(math.pi)*(r*2)
volume = (4/3)*(math.pi)*(r**3)

# output
print("r : ",r)
print("luas : ",luas)
print("volume : ",volume)
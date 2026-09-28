import math

luas_lingkaran = lambda r: math.pi * r ** 2

jari_jari = float(input("Masukkan jari-jari: "))
hasil = luas_lingkaran(jari_jari)
print("Luas lingkaran dengan jari-jari", jari_jari, "=", round(hasil, 2))
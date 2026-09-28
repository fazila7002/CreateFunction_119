def converts_temperature(value, unit):
    if unit == "C":
        return value * 9 / 5 + 32
    elif unit == "F":
        return (value - 32) * 5/9 

input_value = int(input("Masukkan value: "))
input_unit = input("Masukkan unit (C/F): ")
   
konversi = converts_temperature(input_value, input_unit)

if input_unit == "C":
    print(input_value, "C =", konversi, "F")
else:
    print(input_value, "F =", konversi, "C")
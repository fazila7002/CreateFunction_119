def converts_temperature(value, unit):
    if unit == "C":
        return value * 9 / 5 + 32
    elif unit == "F":
        return (value - 32) * 5/9 
   

print(converts_temperature(100, "C"))
print(converts_temperature(212, "F"))
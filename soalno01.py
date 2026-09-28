def converts_temperature(value, unit):
    if unit == "C":
        return value * 9 / 5 + 32

print(converts_temperature(100, "C"))
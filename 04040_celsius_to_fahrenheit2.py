def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "lowest possible temperature is -273.15"
    else:
        return celsius * 9/5 + 32

print(celsius_to_fahrenheit(10))
print(celsius_to_fahrenheit(-273.16))

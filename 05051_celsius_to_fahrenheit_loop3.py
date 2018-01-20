def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "lowest possible temperature is -273.15"
    else:
        return celsius * 9/5 + 32

temperatures = [10, -20, -289, 100]
for temp in temperatures:
    print(celsius_to_fahrenheit(temp))

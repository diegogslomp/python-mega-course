def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32
print(fahrenheit)

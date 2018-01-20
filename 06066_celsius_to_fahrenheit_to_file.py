def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        print "lowest possible temperature is -273.15"
    else:
        print celsius * 9/5 + 32
        with open('temperature.txt', 'a') as file:
            file.write(str(celsius * 9/5 + 32) + '\n')

temperatures = [10, -20, -289, 100]
for temp in temperatures:
    celsius_to_fahrenheit(temp)

numbers = [1, 2, 3]
file = open('output.txt', 'w')

for number in numbers:
    file.write(str(number) + "\n")

file.close()

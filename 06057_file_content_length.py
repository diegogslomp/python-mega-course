file = open('fruits.txt', 'r')
content = file.readlines()
file.close()
fruits = [line.rstrip("\n") for line in content]
for fruit in fruits:
    print(len(fruit))


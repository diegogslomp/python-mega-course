try:
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))
    if width == length:
        print("This looks like a square")
    area = width * length
    print(area)
except ValueError:
    print("Please enter a number")

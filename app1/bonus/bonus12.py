def convert(feet_inches):
    feet, inches = feet_inches.split()
    meters = float(feet) * 0.3048 + float(inches) * 0.0254
    return meters


feet_inches = input("Enter feet and inches: ")
result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")

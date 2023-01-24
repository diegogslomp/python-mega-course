def parse(feet_inches):
    feet, inches = feet_inches.split()
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = float(feet) * 0.3048 + float(inches) * 0.0254
    return meters


feet_inches = input("Enter feet and inches: ")
parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])

print(
    f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters"
)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")

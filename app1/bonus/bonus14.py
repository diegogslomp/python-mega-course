import parser14 as parser
import converter14 as converter

feet_inches = input("Enter feet and inches: ")
parsed = parser.parse(feet_inches)
result = converter.convert(parsed["feet"], parsed["inches"])

print(
    f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters"
)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")

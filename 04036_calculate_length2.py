def calculate_length(string):
    if type(string) == int:
        return "Sorry integers don't have length"
    else:
        return len(string)

print(calculate_length("Hello"))
print(calculate_length(20))

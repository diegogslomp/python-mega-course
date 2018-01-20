def calculate_length(string):
    if type(string) == int:
        return "Sorry integers don't have length"
    elif type(string) == float:
        return "Sorry floats don't have length"
    else:
        return len(string)

print(calculate_length("Hello"))
print(calculate_length(20))
print(calculate_length(20.5))

password = input("Enter password: ")

result = {}

length = False
if len(password) >= 8:
    length = True
result["lenght"] = length

uppercase = False
for letter in password:
    if letter.isupper():
        uppercase = True
        break
result["uppercase"] = uppercase

digit = False
for letter in password:
    if letter.isdigit():
        digit = True
        break
result["digit"] = digit

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")

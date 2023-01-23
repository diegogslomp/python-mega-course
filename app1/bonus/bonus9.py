password = input("Enter new password: ")


result = {}

length = False
if len(password) >= 8:
    length = True
result["length"] = length

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["uppercase"] = uppercase

lowercase = False
for i in password:
    if i.islower():
        lowercase = True
result["lowercase"] = lowercase

print(result)
if all(result.values()):
    print("Strong password")
else:
    print("Weak password")

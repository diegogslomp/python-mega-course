password = input("Enter new password: ")

if len(password) > 7:
  print("Great password there!")
elif len(password) == 7:
  print("Password is OK, but not too strong")
else:
  print("You password is weak")
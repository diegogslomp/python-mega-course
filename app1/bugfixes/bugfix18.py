temperatures = [10, 12, 14]

lines = [f"{t}\n" for t in temperatures]

with open("file.txt", 'w') as file:
  file.writelines(lines)
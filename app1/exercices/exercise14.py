import os

file_path = os.path.join("files", "essay.txt")

with open(file_path, "r") as file:
    print(file.read().title())

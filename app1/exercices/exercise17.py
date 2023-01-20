import os

filenames = ("a.txt", "b.txt", "c.txt")

files_dir = "files"

for filename in filenames:
    file_path = os.path.join(files_dir, filename)
    with open(file_path, "r") as file:
        print(file.read())

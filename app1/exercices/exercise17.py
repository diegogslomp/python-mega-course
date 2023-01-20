import os
import pathlib

filenames = ("a.txt", "b.txt", "c.txt")

files_dir = os.path.join(
    pathlib.Path(os.path.dirname(__name__)).parent.absolute(), "files"
)

for filename in filenames:
    file_path = os.path.join(files_dir, filename)
    with open(file_path, "r") as file:
        print(file.read())

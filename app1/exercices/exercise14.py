import os
import pathlib

file_path = os.path.join(
    pathlib.Path(os.path.dirname(__name__)).parent.absolute(),
    "files",
    "essay.txt",
)

with open(file_path, "r") as file:
    print(file.read().title())

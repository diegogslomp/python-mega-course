import os
import pathlib

file_path = os.path.join(
    pathlib.Path(os.path.dirname(__name__)).parent.absolute(), "files", "members.txt"
)

new_member = input("Enter the new member: ")

with open(file_path, "a") as file:
    file.write(f"{new_member}\n")

import os

file_path = os.path.join("files", "members.txt")

new_member = input("Enter the new member: ")

with open(file_path, "a") as file:
    file.write(f"{new_member}\n")

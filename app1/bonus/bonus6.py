import os
import pathlib

current_dir = os.path.dirname(__file__)
parent_dir = pathlib.Path(current_dir).parent.absolute()
files_dir = os.path.join(parent_dir, "files")

contents = [
    "content file ssssssss aaaaa 1 " "continue " "in another line",
    "file sssssssss 2 content",
    "3 content file",
]
files = ["doc.txt", "report.txt", "presentation.txt"]

for content, file in zip(contents, files):
    file_path = os.path.join(files_dir, file)
    with open(file_path, "w") as file:
        file.write(f"{content}\n")

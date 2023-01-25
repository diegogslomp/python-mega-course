import glob
import os

filespath = os.path.join("files", "*.txt")
myfiles = glob.glob(filespath)

for filepath in myfiles:
    with open(filepath, "r") as file:
        print(file.read().upper())

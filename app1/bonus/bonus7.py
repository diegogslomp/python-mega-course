filenames = ["1.doc", "2.report", "3.presentation"]

fullfilenames = [f"{filename.replace('.','-')}.txt" for filename in filenames]

print(fullfilenames)

filenames = ["1.RAW Reports.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
  filename = filename.replace(".", "-", 1)
  print(filename)
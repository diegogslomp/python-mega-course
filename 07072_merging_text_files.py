import datetime
import glob2

files = glob2.glob('file*.txt')

output = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt")

with open(output, 'a') as out:
    for file in files:
        with open(file) as fil:
            out.write(fil.read() + '\n')


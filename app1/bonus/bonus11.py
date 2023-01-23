import os


def get_average() -> float:
    filename = os.path.join(os.path.curdir, "files", "temperatures.txt")

    with open(filename) as file:
        lines = file.readlines()
        data = [int(line.strip()) for line in lines[1:]]
        average = sum(data) / len(data)
        return average


average = get_average()
print(average)

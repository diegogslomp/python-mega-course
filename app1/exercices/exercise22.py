while True:

    sides = []

    with open("files/sides.txt", "r") as file:
        lines = file.readlines()
        sides = [line.strip() for line in lines]

    side = input("Throw the coin and enter head, tail or other to exit: ")

    if side not in ("head", "tail"):
      break


    sides.append(side)

    nr_heads = sides.count("head")
    percentage = nr_heads / len(sides) * 100

    with open("files/sides.txt", "w") as file:
        lines = [f"{side}\n" for side in sides]
        file.writelines(lines)

    print(f"Heads: {percentage}%")

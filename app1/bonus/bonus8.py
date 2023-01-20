date = input("Enter today's date: ")
mood = input("How do you rate your mood from 1 to 10? ")
though = input("Let your thoughs flow:\n")

with open(f"journal/{date}.txt", "w") as file:
    file.write(f"Mood: {mood}\n\n")
    file.write(f"{though}\n")

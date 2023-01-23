try:
    total = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = value / total * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Please run the program again.")
except ZeroDivisionError:
    print("Your total value can not be zero.")

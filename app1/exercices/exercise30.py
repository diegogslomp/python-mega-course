def number_of_names_given(names):
    return len(names.split(","))


names = input("Enter names separated by commas (no spaces): ")

print(number_of_names_given(names))

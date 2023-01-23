import os

file_path = os.path.join(os.path.curdir, "files", "todos.txt")


def read_from_file() -> list:
    with open(file_path, "r") as file:
        lines = file.readlines()
        todos = [line.strip() for line in lines]
    return todos


def save_to_file(todos: list) -> None:
    with open(file_path, "w") as file:
        lines = [f"{todo}\n" for todo in todos]
        file.writelines(lines)


while True:

    user_input = input("Type add, show, edit, complete or exit: ")
    user_input = user_input.strip()
    user_input = user_input.split()
    user_action = user_input[0]

    match user_action:
        case "add" | "new":
            if len(user_input) > 1:
                todo = " ".join(user_input[1:])
            else:
                todo = input("Enter new todo: ")
                if len(todo) == 0:
                    print("Empty todo not added")
                    continue
            todos = read_from_file()
            todos.append(todo)
            save_to_file(todos)

        case "show":
            todos = read_from_file()
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")

        case "edit":
            try:
                if len(user_input) > 1:
                    number = int(user_input[1])
                else:
                    number = int(input("Number of the todo to edit: "))
                if len(user_input) > 2:
                    new_todo = " ".join(user_input[2:])
                else:
                    new_todo = input("Enter new todo: ")
                todos = read_from_file()
                todos[number - 1] = new_todo
                save_to_file(todos)
            except (ValueError, IndexError):
                print("Invalid todo")

        case "complete" | "delete":
            try:
                if len(user_input) > 1:
                    number = int(user_input[1])
                else:
                    number = int(input("Number of the todo to complete: "))
                todos = read_from_file()
                todos.pop(number - 1)
                save_to_file(todos)
            except (ValueError, IndexError):
                print("Invalid todo")

        case "exit":
            break

        case other:
            print("Invalid command")

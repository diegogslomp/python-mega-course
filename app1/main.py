import os

file_path = os.path.join(os.path.dirname(__file__), "files", "todos.txt")


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

    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:

        case "add":
            todo = input("Enter new todo: ")
            todos = read_from_file()
            todos.append(todo)
            save_to_file(todos)

        case "show":
            todos = read_from_file()
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}".strip())

        case "edit":
            number = int(input("Number of the todo to edit: "))
            todos = read_from_file()
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo
            save_to_file(todos)

        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos = read_from_file()
            todos.pop(number - 1)
            save_to_file(todos)

        case "exit":
            break

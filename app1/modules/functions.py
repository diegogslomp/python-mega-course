import os

file_path = os.path.join(os.path.curdir, "files", "todos.txt")

def get_todos(file_path=file_path) -> list:
    """Return list of todos from file"""
    with open(file_path, "r") as file:
        lines = file.readlines()
        todos = [line.strip() for line in lines]
    return todos


def write_todos(todos: list, file_path=file_path) -> None:
    """Write todos list to file"""
    with open(file_path, "w") as file:
        lines = [f"{todo}\n" for todo in todos]
        file.writelines(lines)

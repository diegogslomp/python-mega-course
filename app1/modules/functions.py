import os

FILEPATH = os.path.join(os.path.curdir, "files", "todos.txt")

def get_todos(filepath=FILEPATH) -> list:
    """Return list of todos from file"""
    with open(filepath, "r") as file:
        lines = file.readlines()
        todos = [line.strip() for line in lines]
    return todos


def write_todos(todos: list, filepath=FILEPATH) -> None:
    """Write todos list to file"""
    with open(filepath, "w") as file:
        lines = [f"{todo}\n" for todo in todos]
        file.writelines(lines)

todos = []

while True:

    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:

        case "add":
            todo = input("Enter new todo: ")
            todos.append(todo)

        case "show":
            for index, item in enumerate(todos):
                number = index + 1
                print(f"{number}. {item}")

        case "edit":
            number = int(input("Number of the todo to edit: "))
            index = number - 1
            if index > (len(todos) - 1) or index < 0:
                print("Unknown todo")
                continue

            new_todo = input("Enter new todo: ")
            todos[index] = new_todo

        case "complete":
            number = int(input("Number of the todo to complete: "))
            index = number - 1
            todos.pop(index)

        case "exit":
            break

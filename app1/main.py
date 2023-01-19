todos = []

while True:

    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:

        case "add":
            todo = input("Enter new todo: ")
            todos.append(todo)

        case "show":
            for item in todos:
                print(item)

        case "edit":
            number = int(input("Number of the todo to edit: "))
            index = number -1

            if index > (len(todos) - 1) or index < 0:
                print("Unknown todo")
                continue

            new_todo = input("Enter new todo: ")
            todos[index] = new_todo

        case "exit":
            break

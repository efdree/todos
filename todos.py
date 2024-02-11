id = 0
tasks = [{"id": (id := id + 1), "content": "Fill the weekly feedback",
          "completed": True},
         {"id": (id := id + 1), "content": "Complete Python Basics 1",
          "completed": False},
         {"id": (id := id + 1), "content": "Complete Python 2",
          "completed": False},
         {"id": (id := id + 1), "content": "Complete Python Methods",
          "completed": False},
         {"id": (id := id + 1), "content": "Do Meditation", "completed": False}]

options = ["add", "list", "completed", "toggle", "delete", "exit"]


def print_options():
    print("\n" + "-"*64 + "\n")
    for option in options:
        if option != "exit":
            print(f"{option} | ", end="")
        else:
            print(f"{option} \n")


def print_tasks(tasks, completed="no"):
    for task in tasks:
        if completed == "no":
            if task["completed"] == False:
                print(f"{task['id']}. {task['content'].capitalize()}")
        elif completed == "yes":
            if task["completed"] == True:
                print(f"{task['id']}. {task['content'].capitalize()}")
        elif completed == "all":
            print(f"{task['id']}. {task['content'].capitalize()}")


def create_task(tasks, content):
    new = {
        "id": tasks[len(tasks) - 1]["id"] + 1,
        "content": content,
        "completed": False
    }
    tasks.append(new)


def delete_task(tasks, id):
    tasks[:] = [task for task in tasks if str(task["id"]) not in id]


def toggle_tasks(tasks, toggle):
    print(toggle)
    for id in toggle:
        found_task = next(
            (task for task in tasks if str(task["id"]) == id), None)
        if found_task:
            if found_task["completed"] == False:
                found_task["completed"] = not found_task["completed"]
        else:
            print("Try again with a valid IDs")
            print("\n" + "-"*64 + "\n")
            print_tasks(tasks, "no")


print("-"*24 + "Welcome to toDOS" + "-"*24 + "\n")
print_tasks(tasks, "no")
print_options()

action = None
while action != "exit":
    action = input("action: ")

    if action == "add":
        content = ""
        while content == "":
            content = input("content: ")
        create_task(tasks, content)
        print_options()
    elif action == "list":
        print("\n" + "-"*64 + "\n")
        print_tasks(tasks, "all")
        print_options()
    elif action == "completed":
        print("\n" + "-"*64 + "\n")
        print_tasks(tasks, "yes")
        print_options()
    elif action == "toggle":
        print("\n" + "-"*64 + "\n")
        toggle = ""
        while toggle == "":
            toggle = input("todo ID: ").split(", ")
        toggle_tasks(tasks, toggle)
        print_options()
    elif action == "delete":
        id = ""
        while id == "":
            id = input("todo ID: ")
        delete_task(tasks, id)
        print_options()
    elif action == "exit":
        print("Thanks for using toDOS!")

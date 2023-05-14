tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

def show_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

while True:
    print("Select an option:")
    print("01. Add task")
    print("02. Remove task")
    print("03. Show tasks")
    print("04. Exit")
    choice = input("> ")

    if choice == "01":
        add_task()
    elif choice == "02":
        remove_task()
    elif choice == "03":
        show_tasks()
    elif choice == "04":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

def show_menu():
    print("\n--- TO-DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")
    except:
        print("Invalid input!")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")

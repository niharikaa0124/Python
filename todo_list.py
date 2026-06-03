import json
tasks = []

def load_tasks():
    global tasks

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task_name = input("Enter task: ")

    tasks.append({
        "task": task_name,
        "done": False
    })

    save_tasks()
    print("Task added successfully")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found")
        return

    print("\n===== TASKS =====")

    for i, task in enumerate(tasks, start=1):

        status = "✓" if task["done"] else " "

        print(f"{i}. [{status}] {task['task']}")

def mark_complete():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        index = int(input("Enter task number: ")) - 1

        tasks[index]["done"] = True

        save_tasks()

        print("Task marked as completed")

    except (ValueError, IndexError):
        print("Invalid task number")

def remove_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        index = int(input("Enter task number: ")) - 1

        removed = tasks.pop(index)

        save_tasks()

        print(f"Removed: {removed['task']}")

    except (ValueError, IndexError):
        print("Invalid task number")

def show_stats():

    completed = 0

    for task in tasks:
        if task["done"]:
            completed += 1

    print(f"""
Total Tasks     : {len(tasks)}
Completed Tasks : {completed}
Pending Tasks   : {len(tasks) - completed}
""")

load_tasks()

while True:

    print("""
===== TO-DO APP =====

1. Add Task
2. View Tasks
3. Mark Complete
4. Remove Task
5. Statistics
6. Exit

=====================
""")

    choice = input("Choose option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        mark_complete()

    elif choice == "4":
        remove_task()

    elif choice == "5":
        show_stats()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
import time

# List to store tasks
tasks = []
next_id = 1  


# Function to add a new task
def add_task():
    global next_id  

    name = input("Enter the task name: ").lower()

    try:
        priority = int(input("Enter priority (1 = highest, 5 = lowest): "))
    except ValueError:
        print("Invalid priority.")
        return

    task = {
        "id": next_id,
        "name": name,
        "priority": priority,
        "done": False
    }

    tasks.append(task)
    next_id += 1  

    print("Task created successfully.")


# Function to remove a task
def remove_task():
    if not tasks:
        print("No tasks registered.")
        return

    list_tasks()

    try:
        task_id = int(input("Enter the ID of the task to remove: "))
    except ValueError:
        print("Invalid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task removed successfully.")
            return

    print("Task not found.")


# Function to update task priority
def update_task():
    if not tasks:
        print("No tasks registered.")
        return

    list_tasks()

    try:
        task_id = int(input("Enter the ID of the task to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            try:
                priority = int(input("Enter new priority (1-5): "))
            except ValueError:
                print("Invalid priority.")
                return

            task["priority"] = priority
            print("Task updated successfully.")
            return

    print("Task not found.")


# Function to mark a task as done
def complete_task():
    if not tasks:
        print("No tasks registered.")
        return

    list_tasks()

    try:
        task_id = int(input("Enter the ID of the task to mark as done: "))
    except ValueError:
        print("Invalid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print("Task marked as completed.")
            return

    print("Task not found.")


# Function to display all tasks
def list_tasks():
    if not tasks:
        print("No tasks registered.")
        return

    print("\n=== TASK LIST ===\n")

    for task in tasks:
        status = "✔ Done" if task["done"] else "✖ Pending"
        print(f"[{task['id']}] {task['name']} | Priority: {task['priority']} | {status}")


# Function to display menu
def menu():
    print("\n" + "=" * 40)
    print("TASK MANAGER CLI")
    print("=" * 40)
    print("1 - Add Task")
    print("2 - Remove Task")
    print("3 - Update Task Priority")
    print("4 - Show Tasks")
    print("5 - Complete Task")
    print("6 - Exit")
    print("=" * 40)


# Mapping options to functions
options = {
    1: add_task,
    2: remove_task,
    3: update_task,
    4: list_tasks,
    5: complete_task
}


# Validate and execute option
def handle_option(choice):
    if choice in options:
        options[choice]()
    else:
        print("Please choose a valid option.")


# Main loop
while True:
    menu()

    try:
        choice = int(input("Choose an option: "))

        if choice == 6:
            print("Goodbye!")
            break

        handle_option(choice)

    except ValueError:
        print("Please enter a valid number.")
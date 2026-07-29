def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\n------ TO-DO LIST ------")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def update_task(tasks):
    """Update an existing task."""
    if not tasks:
        print("No tasks available to update.")
        return

    display_tasks(tasks)

    try:
        task_num = int(input("Enter task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new task: ").strip()
            if new_task:
                tasks[task_num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    """Delete a task."""
    if not tasks:
        print("No tasks available to delete.")
        return

    display_tasks(tasks)

    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\nThank you for using the To-Do List Application!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

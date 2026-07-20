"""
DecodeLabs - Python Programming Industrial Training Kit
Project 1: The To-Do List

Goal: Build a program where users can add tasks to a list and view them.
Key Skill: Lists (append & print loops).
"""


def display_menu():
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    print("===============================")


def add_task(my_tasks):
    task = input("Enter the task you want to add: ").strip()
    if task:
        my_tasks.append(task)
        print(f"✅ Task added: '{task}'")
    else:
        print("⚠️  Task cannot be empty. Please try again.")


def view_tasks(my_tasks):
    print("\n--- YOUR TASKS ---")
    if not my_tasks:
        print("No tasks yet. Add one from the menu!")
    else:
        # enumerate() gives simultaneous access to index (ID) and value (data)
        for index, task in enumerate(my_tasks, start=1):
            print(f"{index}. {task}")
    print("------------------")


def remove_task(my_tasks):
    view_tasks(my_tasks)
    if not my_tasks:
        return
    try:
        choice = int(input("Enter the task number to remove: "))
        if 1 <= choice <= len(my_tasks):
            removed = my_tasks.pop(choice - 1)
            print(f"🗑️  Removed: '{removed}'")
        else:
            print("⚠️  Invalid task number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")


def main():
    # This is our storage: an empty list that holds multiple tasks
    # in a single variable — the foundation of every database.
    my_tasks = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(my_tasks)
        elif choice == "2":
            view_tasks(my_tasks)
        elif choice == "3":
            remove_task(my_tasks)
        elif choice == "4":
            print("👋 Goodbye! Keep building.")
            break
        else:
            print("⚠️  Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()

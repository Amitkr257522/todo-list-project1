# Project 1 - To Do List
# DecodeLabs internship task
# basically storing tasks in a list and letting user add/view/remove them

my_tasks = []  # empty list to start, this is where all tasks will live


def show_menu():
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")


def add_task():
    task = input("What's the task? ")
    task = task.strip()

    if task == "":
        print("can't add empty task")
        return

    my_tasks.append(task)
    print("added:", task)


def view_tasks():
    print("\nYour tasks:")
    if len(my_tasks) == 0:
        print("nothing here yet")
        return

    # using enumerate so i get both number and the task, saw this online
    # instead of doing range(len(my_tasks))
    for i, t in enumerate(my_tasks, 1):
        print(i, "-", t)


def remove_task():
    view_tasks()
    if len(my_tasks) == 0:
        return

    num = input("Enter task number to remove: ")

    # wrapped in try except cause if someone types letters it was crashing before
    try:
        num = int(num)
    except ValueError:
        print("enter a number please")
        return

    if num < 1 or num > len(my_tasks):
        print("invalid task number")
        return

    removed = my_tasks.pop(num - 1)
    print("removed:", removed)


# main loop
while True:
    show_menu()
    choice = input("Pick an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("👋 Goodbye! Keep building.")
        break
    else:
        print("that's not a valid option")

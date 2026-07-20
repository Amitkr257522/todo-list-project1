# 📝 To-Do List Manager — Project 1

**DecodeLabs Python Programming | Industrial Training Kit | Batch 2026**

## 📌 Overview
A menu-driven console program that lets a user **add**, **view**, and **remove** tasks stored in a Python list. This is the foundational "in-memory database" exercise — before working with real databases, you must first master storing multiple items in a single variable.

## 🎯 Goal
Build a program where users can add tasks (e.g., "Finish Python assignment") to a list and view them.

## 🧠 Key Concepts Used
| Concept | Where it's used |
|---|---|
| **Lists as storage** | `my_tasks = []` — the "in-memory database" holding all tasks |
| **append()** | Adds new tasks to the list dynamically |
| **enumerate()** | Displays tasks with both index (ID) and value (data) simultaneously — the "professional" way instead of `range(len(...))` |
| **Loops** | `while True:` menu loop keeps the program running until the user exits |
| **Defensive Coding** | `try/except ValueError` when removing a task by number, so invalid input doesn't crash the program |
| **Functions** | Logic separated into `add_task()`, `view_tasks()`, `remove_task()`, `display_menu()` for clean, modular code |

## ▶️ How to Run
```bash
python todo_list.py
```

## 💻 Sample Run
```
===== TO-DO LIST MANAGER =====
1. Add a task
2. View tasks
3. Remove a task
4. Exit
===============================
Choose an option (1-4): 1
Enter the task you want to add: Finish Python assignment
✅ Task added: 'Finish Python assignment'

Choose an option (1-4): 2

--- YOUR TASKS ---
1. Finish Python assignment
------------------

Choose an option (1-4): 4
👋 Goodbye! Keep building.
```

## 🛡️ Error Handling
- **Empty task input** → rejected with a warning, user asked to try again
- **Invalid task number while removing** → caught by `except ValueError`, no crash
- **Out-of-range task number** → handled gracefully with a warning message

## 📂 Files
- `todo_list.py` — main script

## 🏢 About
Built as part of the **DecodeLabs Industrial Training Kit — Project 1 (Week 1)**.

📧 decodelabs.tech@gmail.com | 🌎 www.decodelabs.tech

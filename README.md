# 🧠 TaskTrackerCLI

A simple **Command Line Interface (CLI)** tool to help you track and manage your daily tasks efficiently.  
Easily **add**, **update**, **delete**, and **track progress** of your tasks — all directly from the terminal.

---

## 🚀 Features

✅ Add, update, and delete tasks  
✅ Mark tasks as **done** or **in progress**  
✅ List tasks by status (done, in progress, not done)  
✅ Data persistence using JSON  
✅ Simple, clean CLI interface  

---

## 🧩 Commands

| Command | Description |
|----------|--------------|
| y task_tracker.py add "Task description"` | Add a new task |
| py task_tracker.py update <id> "New description"` | Update a task |
| py task_tracker.py delete <id>` | Delete a task |
| py task_tracker.py mark-in-progress <id>` | Mark task as in progress |
| py task_tracker.py mark-done <id>` | Mark task as done |
| py task_tracker.py list` | List all tasks |
| py task_tracker.py list done` | List done tasks |
| py task_tracker.py list not-done` | List not done tasks |
| py task_tracker.py list in-progress` | List in-progress tasks |

---

## 💾 Example Usage

py task_tracker.py add "Finish the CLI project"
py task_tracker.py mark-in-progress 1
py task_tracker.py mark-done 1
py task_tracker.py list done

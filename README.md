# 🧠 TaskTrackerCLI

A simple **Command Line Interface (CLI)** tool to help you track and manage your daily tasks efficiently.  
Easily **add**, **update**, **delete**, and **track progress** of your tasks — all directly from the terminal.

> 📚 This project is based on the [Task Tracker project on roadmap.sh](https://roadmap.sh/projects/task-tracker).  
> It was developed as part of my learning journey to improve programming skills and work with CLI applications in Python.

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
| `python task_tracker.py add "Task description"` | Add a new task |
| `python task_tracker.py update <id> "New description"` | Update a task |
| `python task_tracker.py delete <id>` | Delete a task |
| `python task_tracker.py mark-in-progress <id>` | Mark task as in progress |
| `python task_tracker.py mark-done <id>` | Mark task as done |
| `python task_tracker.py list` | List all tasks |
| `python task_tracker.py list done` | List done tasks |
| `python task_tracker.py list not-done` | List not done tasks |
| `python task_tracker.py list in-progress` | List in-progress tasks |

---

## 💾 Example Usage

```bash
python task_tracker.py add "Finish the CLI project"
python task_tracker.py mark-in-progress 1
python task_tracker.py mark-done 1
python task_tracker.py list done

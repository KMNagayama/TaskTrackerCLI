import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": description,
        "status": "not done",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: [{task_id}] {description}")


def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks(tasks)
            print(f"✏️ Task {task_id} updated.")
            return
    print("Task not found.")


def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")


def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            save_tasks(tasks)
            print(f"🚀 Task {task_id} marked as '{status}'.")
            return
    print("Task not found.")


def list_tasks(filter_status=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    filtered = tasks
    if filter_status:
        filtered = [t for t in tasks if t["status"] == filter_status]

    for task in filtered:
        print(f"[{task['id']}] {task['description']} - {task['status']}")
    print(f"\nTotal: {len(filtered)} task(s).")


def main():
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task description.")
        else:
            add_task(" ".join(sys.argv[2:]))

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: update <id> <new description>")
        else:
            update_task(int(sys.argv[2]), " ".join(sys.argv[3:]))

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: delete <id>")
        else:
            delete_task(int(sys.argv[2]))

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: mark-in-progress <id>")
        else:
            mark_task(int(sys.argv[2]), "in progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: mark-done <id>")
        else:
            mark_task(int(sys.argv[2]), "done")

    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        else:
            status_map = {
                "done": "done",
                "not-done": "not done",
                "in-progress": "in progress"
            }
            filter_status = status_map.get(sys.argv[2], None)
            if filter_status:
                list_tasks(filter_status)
            else:
                print("Unknown list option.")

    else:
        print("Unknown command.")


if __name__ == "__main__":
    main()

import os

FILENAME = "tasks.txt"

def load_tasks():
    tasks = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) >= 3:
                    task_id = parts[0]
                    title = parts[1]
                    status = parts[2]
                    priority = parts[3] if len(parts) > 3 else "N/A"
                    tasks[int(task_id)] = {"title": title, "status": status, "priority": priority}
    return tasks

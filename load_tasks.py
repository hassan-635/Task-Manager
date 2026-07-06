import os

FILENAME = "tasks.txt"

def load_tasks():
    tasks = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split(" | ")
                tasks[(task_id)] = {"title": title, "status": status}
    return tasks

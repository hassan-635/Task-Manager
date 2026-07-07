FILENAME = "tasks.txt"

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")
            
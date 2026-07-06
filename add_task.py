

def add_task(tasks):
    title = input("Enter Task Title : ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task {title} added...")
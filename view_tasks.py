
def view_tasks(tasks):
    if not tasks:
        print("No task Available...")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] -> {task['title']} -> {task['status']} -> {task.get('priority', 'N/A')}")
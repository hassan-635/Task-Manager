

def delete_task(tasks):
    task_id = int(input("Please Enter Task ID : "))
    if task_id in tasks:
        deleted_tasks = tasks.pop(task_id)
        print(f"Task {deleted_tasks["title"]} Deleted...")
    else:
        print(f"TAsk {task_id} Not Found...")
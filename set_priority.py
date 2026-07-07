

def set_priority(tasks):
    task_id = input("Please Enter Task Id : ")
    task_id = int(task_id)
    if task_id in tasks:
        priority = input("Please Enter priority (H/L) : ")
        tasks[task_id]["priority"] = priority
        print("Task Priority set...")

    else:
        print("No Task Available ...")

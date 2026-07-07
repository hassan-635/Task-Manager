

def set_priority(tasks, priority):
    task_id = int(input("Please Enter Task Id : "))
    if task_id in tasks:
        tasks[task_id]["priority"] = priority
        print("Task Priority set...")
    else:
        print("No Task Available ...")
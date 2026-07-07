

def set_priority(tasks):
    task_id = int(input("Please Enter Task Id : "))
    if task_id in tasks:
        priority = input("Please Enter priority (H/L) : ")
        tasks[task_id]["priority"] = priority
        print("Task Priority set...")
    else:
        print("No Task Available ...")
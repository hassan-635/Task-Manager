
def mark_task(tasks):
    task_id = int(input("Please Enter Task id to mark as Complete : "))
    if task_id in tasks:
        tasks[task_id]["status"] = "Completed"
        print(f"Task Id {task_id} marksd as Complete ...")
    else:
        print(f"Task Id {task_id} Not found!!!")
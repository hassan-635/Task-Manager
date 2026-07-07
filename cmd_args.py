import argparse
import add_task as at
import save_tasks as st

# Step 2: Parser Create Karna
parser = argparse.ArgumentParser(description="Command Line Task Manager")


# step 3 arguments add krna

parser.add_argument("--add", type=str, help="Add new task") # string argument
parser.add_argument("--delete", type=int, help="Delete task by id")
parser.add_argument("--export-json", help="export json file")
parser.add_argument("--mark-task", type=int, help="Mark task as completed")
parser.add_argument("--set-priority", nargs=2, help="Set task priority")
parser.add_argument("--view",action="store_true" ,help="View tasks") # boolean flag


# step 4 parse the arguments
# it reads command line and store arguments in args object

args = parser.parse_args()

#sstep 5 handle arguments

if args.add:
    tasks = at.add_task(args.add)
    st.save_tasks(tasks)
    print(f"Task {args.add} added successfully")

if args.delete:
    tasks = st.load_tasks()
    tasks = [task for task in tasks if task["id"] != args.delete]
    st.save_tasks(tasks)
    print(f"Task {args.delete} deleted successfully")

if args.export_json:
    tasks = st.load_tasks()
    st.save_tasks(tasks, args.export_json)
    print(f"Tasks exported to {args.export_json}")

if args.mark_task:
    tasks = st.load_tasks()
    for task in tasks:
        if task["id"] == args.mark_task:
            task["completed"] = True
            break
    st.save_tasks(tasks)
    print(f"Task {args.mark_task} marked as completed")

if args.set_priority:
    tasks = st.load_tasks()
    for task in tasks:
        if task["id"] == int(args.set_priority[0]):
            task["priority"] = args.set_priority[1]
            break
    st.save_tasks(tasks)
    print(f"Task {args.set_priority[0]} priority set to {args.set_priority[1]}")

if args.view:
    tasks = st.load_tasks()
    for task in tasks:
        print(task)
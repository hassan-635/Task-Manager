import argparse

# Step 2: Parser Create Karna
parser = argparse.ArgumentParser(description="Command Line Task Manager")


# step 3 arguments add krna

parser.add_argument("--add", type=str, help="Add new task")
parser.add_argument("--delete", type=int, help="Delete task by id")
parser.add_argument("--export-json", help="export json file")
parser.add_argument("--mark-task", type=int, help="MArk task as completed")
parser.add_argument("--set-priority", nargs=2, help="Set task priority")
parser.add_argument("--view", help="View tasks")
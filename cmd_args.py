import argparse

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
from load_tasks import load_tasks 
from add_task import add_task as at
from view_tasks import view_tasks as vt
from mark_task_completed import mark_task as mt
from delete_task import delete_task as dt
from save_tasks import save_tasks as st

def main():
    tasks = load_tasks()
    while True:
        print("\n\n______________________________________________________Task Manager____________________________________________________\n\n")
        print("1. Add Task\n2. View Tasks\n3. Mark Task As Complete\n4. Delete Task\n5. Exit")
        choice = int(input("Please Enter above Option(1 -> 5) : "))

        if choice == 1:
            at(tasks)
        elif choice == 2:
            vt(tasks)
        elif choice == 3:
            mt(tasks)
        elif choice == 4:
            dt(tasks)
        elif choice == 5:
            st(tasks)
            print("GoodBye")
            break
        else:
            print("Please Enter a valid option (1 -> 5)")

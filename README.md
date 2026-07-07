# 📋 Task Manager

A simple and elegant command-line Task Manager application built in Python. Manage your daily tasks efficiently with features like adding, viewing, completing, deleting tasks, and setting priorities.

## ✨ Features

- **Add Task** - Create new tasks with custom titles
- **View Tasks** - Display all your tasks in a clean format
- **Mark Complete** - Mark tasks as completed when done
- **Delete Task** - Remove tasks you no longer need
- **Set Priority** - Assign high (H) or low (L) priority to tasks
- **CLI Mode** - Fast command-line operations for power users
- **Export JSON** - Export tasks to JSON format
- **Persistent Storage** - Tasks are saved to `tasks.txt` and loaded automatically

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the application:

```bash
python main_menu.py
```

## 📖 Usage

Once you run the application, you'll see a menu with the following options:

```
1. Add Task
2. View Tasks
3. Mark Task As Complete
4. Delete Task
5. Set Task Priority
6. Exit
```

### Adding a Task
- Select option 1
- Enter the task title
- The task will be added with an auto-generated ID

### Viewing Tasks
- Select option 2
- All tasks will be displayed with their IDs, titles, and status

### Marking Task as Complete
- Select option 3
- Enter the task ID
- The task status will be updated to "complete"

### Deleting a Task
- Select option 4
- Enter the task ID
- The task will be removed from the list

### Setting Task Priority
- Select option 5
- Enter the task ID
- Enter priority (H for High, L for Low)
- The priority will be assigned to the task

### Exiting
- Select option 6
- All tasks will be saved to `tasks.txt`
- The application will close

## ⚡ CLI Mode

For fast operations, use the command-line interface:

```bash
# Add a task
python cmd_args.py --add "Buy groceries"

# View all tasks
python cmd_args.py --view

# Mark task as completed
python cmd_args.py --mark-task 1

# Delete a task
python cmd_args.py --delete 1

# Set task priority
python cmd_args.py --set-priority 1 H

# Export tasks to JSON
python cmd_args.py --export-json tasks.json

# Show help
python cmd_args.py --help
```

### CLI Arguments

- `--add <title>` - Add a new task with the given title
- `--view` - Display all tasks
- `--mark-task <id>` - Mark task as completed by ID
- `--delete <id>` - Delete task by ID
- `--set-priority <id> <priority>` - Set priority (H/L) for task
- `--export-json <filename>` - Export tasks to JSON file

## 📁 Project Structure

```
Task Manager/
├── main_menu.py           # Main application menu (interactive mode)
├── cmd_args.py            # Command-line interface (CLI mode)
├── add_task.py            # Add new tasks
├── view_tasks.py          # View all tasks
├── mark_task_completed.py # Mark tasks as complete
├── delete_task.py         # Delete tasks
├── set_priority.py        # Set task priorities
├── load_tasks.py          # Load tasks from file
├── save_tasks.py          # Save tasks to file
├── tasks.txt              # Data storage file
└── README.md              # This file
```

## 💾 Data Storage

Tasks are stored in `tasks.txt` in the following format:
```
task_id | title | status | priority
```

## 🛠️ Technologies Used

- Python 3.x

## 📝 License

This project is open source and available for educational purposes.

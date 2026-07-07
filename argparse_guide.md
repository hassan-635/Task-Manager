









### Step 4: Arguments Parse Karna
```python
args = parser.parse_args()
```
**Yeh kya karta hai?** - Command line ko read karke arguments ko `args` object mein store karta hai.

### Step 5: Arguments Handle Karna
```python
if args.add:
    # Yahan add task ka logic
    print(f"Task added: {args.add}")

elif args.list:
    # Yahan list tasks ka logic
    print("Listing all tasks...")
```

## 🕐 Kab Use Karna Chahiye?

### ✅ Use Jab:
- User ko fast operations chahiye
- Automation scripts bana rahe ho
- Professional CLI tool bana rahe ho
- Multiple tasks ek saath karna ho

### ❌ Use Na Jab:
- User beginner hai aur interactive interface chahiye
- Complex input validation chahiye
- GUI based application hai

## 💡 Practical Examples

### Example 1: Simple Add Task
```python
# Command: python cmd_args.py --add "Buy milk"
parser.add_argument("--add", type=str, help="Add task")

# Code:
if args.add:
    print(f"Adding task: {args.add}")
```

### Example 2: List Tasks (Flag)
```python
# Command: python cmd_args.py --list
parser.add_argument("--list", action="store_true", help="List tasks")

# Code:
if args.list:
    print("Showing all tasks...")
```

### Example 3: Complete Task (Integer)
```python
# Command: python cmd_args.py --complete 5
parser.add_argument("--complete", type=int, help="Complete task by ID")

# Code:
if args.complete:
    print(f"Marking task {args.complete} as complete")
```

### Example 4: Set Priority (Multiple Values)
```python
# Command: python cmd_args.py --priority 5 H
parser.add_argument("--priority", nargs=2, help="Set priority")

# Code:
if args.priority:
    task_id = args.priority[0]
    priority = args.priority[1]
    print(f"Setting priority {priority} for task {task_id}")
```

## 🛠️ Common Argument Types

| Type | Example | Description |
|------|---------|-------------|
| `type=str` | `--add "task"` | String input |
| `type=int` | `--delete 5` | Integer input |
| `type=float` | `--rate 3.5` | Decimal number |
| `action="store_true"` | `--list` | Boolean flag (True/False) |
| `nargs=2` | `--priority 5 H` | Multiple values |
| `choices=['H','L']` | `--priority H` | Fixed options |

## ⚠️ Important Points

1. **Argument names double dash se start hote hain** (`--add`, `--list`)
2. **Single dash short names** (`-a`, `-l`) bhi de sakte ho
3. **Help message zaroori hai** taake user samajh sake
4. **Type validation important hai** - wrong type pe error dega
5. **Default values set kar sakte ho** - `default="N/A"`

## 🎓 Complete Template

```python
import argparse

def main():
    # 1. Parser create
    parser = argparse.ArgumentParser(description="My CLI Tool")
    
    # 2. Arguments add
    parser.add_argument("--add", type=str, help="Add item")
    parser.add_argument("--list", action="store_true", help="List items")
    parser.add_argument("--delete", type=int, help="Delete by ID")
    
    # 3. Parse arguments
   _args = parser.parse_args()
    
    # 4. Handle arguments
    if args.add:
        print(f"Adding: {args.add}")
    elif args.list:
        print("Listing items...")
    elif args.delete:
        print(f"Deleting: {args.delete}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

## 🔍 Testing Commands

```bash
# Help dekhne ke liye
python cmd_args.py --help

# Task add karne ke liye
python cmd_args.py --add "My new task"

# Tasks list karne ke liye
python cmd_args.py --list

# Task complete karne ke liye
python cmd_args.py --complete 1

# Task delete karne ke liye
python cmd_args.py --delete 1

# Priority set karne ke liye
python cmd_args.py --priority 1 H
```

## 💪 Pro Tips

1. **Error handling** - Try-except use karo for invalid inputs
2. **Validation** - Check karo task ID exists ya nahi
3. **User feedback** - Clear messages print karo
4. **Consistent naming** - Similar naming convention use karo
5. **Documentation** - README mein examples add karo

---

**Happy Learning! 🚀**

import json

def export_json(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    
    print("Json Format exported ...")
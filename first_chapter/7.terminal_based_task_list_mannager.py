
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                task, status = line.strip().rsplit("||", 1)
                if task:
                    tasks.append({"task": task, "status": status == "done"})
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task['task']}||{' done' if task['status'] else ' not_done'}\n")


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["status"] else "✗"
        print(f"{idx}. [{status}] {task['task']}")
    print()

def task_manager():
    tasks = load_tasks()
    
    while True:
        display_tasks(tasks)
        print("Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()

        match choice:
            case "1":
                new_task = input("Enter a new task: ").strip()
                if new_task:
                    tasks.append({"task": new_task, "status": False})
                    save_tasks(tasks)
                    print("Task added successfully!")
                else:
                    print("Task cannot be empty.")
            case "2":
                display_tasks(tasks)
            case "3":
                display_tasks(tasks)
                try:
                    task_num = int(input("Enter the task number to mark as done: "))
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num - 1]["status"] = True
                        save_tasks(tasks)
                        print("Task marked as done!")
                    else:
                        print("Invalid task number.")
            
                except ValueError:
                    print("Please enter a valid number.")
            case "4":
                display_tasks(tasks)
                try:     
                    task_num = int(input("Enter the task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"Task '{removed['task']}' deleted successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:   
                    print("Please enter a valid number.")
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid option. Please choose between 1 and 5.")

task_manager()
        # if choice == "1":
        #     new_task = input("Enter a new task: ").strip()
        #     if new_task:
        #         tasks.append({"task": new_task, "status": False})
        #         save_tasks(tasks)
        #         print("Task added successfully!")
        #     else:
        #         print("Task cannot be empty.")
        
        # elif choice == "2":
        #     try:
        #         task_num = int(input("Enter the task number to mark as done: "))
        #         if 1 <= task_num <= len(tasks):
        #             tasks[task_num - 1]["status"] = True
        #             save_tasks(tasks)
        #             print("Task marked as done!")
        #         else:
        #             print("Invalid task number.")
        #     except ValueError:
        #         print("Please enter a valid number.")
        
        # elif choice == "3":
        #     try:
        #         task_num = int(input("Enter the task number to delete: "))
        #         if 1 <= task_num <= len(tasks):
        #             del tasks[task_num - 1]
        #             save_tasks(tasks)
        #             print("Task deleted successfully!")
        #         else:
        #             print("Invalid task number.")
        #     except ValueError:
        #         print("Please enter a valid number.")
        
        # elif choice == "4":
        #     print("Goodbye!")
        #     break
        # else:
        #     print("Invalid option. Please choose between 1 and 4.")
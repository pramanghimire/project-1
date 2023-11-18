# Create a simple to-do list
tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added.")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task deleted.")
    else:
        print("Task not found.")

def view_tasks():
    if tasks:
        print("Your tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks yet.")

# Test the functions
add_task("Complete project")
add_task("Buy groceries")
view_tasks()
delete_task("Complete project")
view_tasks()

from InquirerPy import inquirer
from datetime import datetime


tasks = []

def add_task():
    
    while True:

        task_id = len(tasks) + 1

        title = input("Enter task title: ")
        priority = input("Add priority(High/Medium/Low)").lower()
        status = "Pending"
        created_at = datetime.now()

        task = {
            "id" : task_id,
            "title" : title,
            "priority": priority,
            "status": status,
            "created_at": created_at
        }

        tasks.append(task)
        print("Task created with Task Id: ", task_id)
        break
    return


def view_tasks():
    print(tasks)

def mark_as_completed(task_id):
    # print(task_id)
    task_idx = None
    for i, task in enumerate(tasks):
        if task.get("id") == task_id:
            task_idx = i
    # print(task_idx)
    task[task_id] = {"status": "completed"}

    print("Task ", task_id, " marked as completed")
    return

def menu():

    while True:
        choice = inquirer.select(
            message="Task Manager",
            choices = [
                "Add task",
                "View all tasks",
                "Mark task as completed",
                "Update task",
                "Delete task",
                "Search tasks",
                "Show task statistics",
                "Exit"
                ]
        ).execute()


        if choice == "Add task":
            add_task()
        elif choice == "View all tasks":
            view_tasks()
        elif choice == "Mark task as completed":
            while True:
                try:
                    task_id = int(input("Enter task id: "))
                    mark_as_completed(task_id)
                    break
                except ValueError:
                    print("Please enter valid id")
                break

        print(choice)

        break

    restart = int(input("restart? "))
    if restart == 1:
        menu()



    

menu()


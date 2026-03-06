# Todo
helps users manage their daily work easily. It allows users to create and store tasks that need to be completed. Each task can have a deadline, helping users finish work on time. Tasks can be marked as completed or pending to track progress. Users can also update or delete tasks if plans change, which improves time management and productivity.
# TODO App using List and Dictionary

tasks = []

def add_task():
    title = input("Enter task name: ")
    deadline = input("Enter deadline (dd-mm-yyyy): ")
    
    task = {
        "title": title,
        "deadline": deadline,
        "completed": False
    }
    
    tasks.append(task)
    print("Task added successfully!\n")


def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i+1}. {task['title']} | Deadline: {task['deadline']} | Status: {status}")
    print()


def mark_completed():
    view_tasks()
    num = int(input("Enter task number to mark completed: "))
    
    if 0 < num <= len(tasks):
        tasks[num-1]["completed"] = True
        print("Task marked as completed!\n")
    else:
        print("Invalid task number\n")


def update_task():
    view_tasks()
    num = int(input("Enter task number to update: "))
    
    if 0 < num <= len(tasks):
        new_title = input("Enter new task name: ")
        new_deadline = input("Enter new deadline: ")
        
        tasks[num-1]["title"] = new_title
        tasks[num-1]["deadline"] = new_deadline
        
        print("Task updated successfully!\n")
    else:
        print("Invalid task number\n")


def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    
    if 0 < num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted successfully!\n")
    else:
        print("Invalid task number\n")


while True:
    print("---- TODO APP ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        update_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")

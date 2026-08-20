from taskstore import *
import sys
tasks=load_data()

if tasks:
    id = max(task["task_id"] for task in tasks) + 1
else:
    id = 1
def menu():
    print("""
========== TO-DO LIST ==========
1. Add Task
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. Mark Task as Completed
6. Update Task
7. Delete Task
8. Search Task
9. Save Tasks
10. Exit
================================""")
    option = int(input("Please select a option "))
    match option:
        case 1:
            title=input("Enter task title: ")
            priority=input("Enter priority (Low/Medium/High):")
            deadline=input("Enter due date (DD-MM-YYYY):")
            add_task(task_title=title,priority=priority,due_tate=deadline)
        case 2:
            display_task()
        case 3:
            view_pending()
        case 4:
            view_completed()
        case 5:
            try:
                completed_task_id = int(input("Enter the task id to mark as completed"))
            except ValueError:
                print("Please enter valid task id")
            else:
                mark_completed(completed_task_id)
        case 6:
            update_task()
        case 7:
            try:
                task_to_remove = int(input("Enter the task id to delete"))
            except ValueError:
                print("enter a valid task id")
            else:
                remove_task(task_to_remove)
        case 8:
            task_to_search=input("Enter the task keyword to search")
            search_by_id(task_to_search)
        case 9:
            save_tasks()
        case 10:
            exit_menu()
def add_task(task_title,priority,due_tate):
    global id
    if not priority_handler(priority):
        raise InvalidPriorityError("Please Enter a Valid Priority:Low,Medium or High")
    if(not date_check(due_tate)):
        raise InvalidDateError("Please enter a date of today or in future")
    tasks.append({
        "task_id":id,
        "task":task_title,
        "task_priority":priority,
        "deadline":due_tate,
        "status":"pending"
    })
    save_data(id=id,task_title=task_title,priority=priority,due_tate=due_tate,status="pending")
    id+=1
def display_task():
    for i in range(len(tasks)):
        print(tasks[i])
def view_pending():
    for i in range(len(tasks)):
        if(tasks[i]["status"]=="pending"):
            print(tasks[i])
def view_completed():
    for i in range(len(tasks)):
        if(tasks[i]["status"]=="completed"):
            print(tasks[i])
def mark_completed(task_id):
    for i in range(len(tasks)):
        if(tasks[i]["task_id"]==task_id):
            tasks[i]["status"]="completed"
def update_task():
    task_to_update = int(input("Please enter the task id to update :"))
    to_update = int(input("""
          Select what you want to update:
          1.Tast title
          2.Task priority
          3.Deadline
          """))
    header_map={
        1:"task",
        2:"task_priority",
        3:"deadline"
    }
    field = header_map[to_update]
    updated_field = input("enter the data to update :")
    for i in range(len(tasks)):
        if(tasks[i]["task_id"]==task_to_update):
            tasks[i][field]=updated_field
    save_all_to_csv(tasks)
    print("Successfully saved data")
def remove_task(task_id):
    for index in range(len(tasks)):
        if(tasks[index]["task_id"]==task_id):
            print(f"Removed this task :{tasks[index]}")
            tasks.pop(index)
            break
    save_all_to_csv(tasks)
def search_by_id(keyword):
    for index in range(len(tasks)):
            if(has_match(re.escape(keyword),tasks[index]["task"])):
                print(tasks[index])
def save_tasks():
    save_all_to_csv(tasks=tasks)
    print("all tasks are saved into csv now")
def exit_menu():
    print("Exiting app...")
    sys.exit()
           
while True:
    menu()

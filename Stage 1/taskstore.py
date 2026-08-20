import csv
import os
import re
import datetime as dt
def save_data(task_title,priority,due_tate,id,status):
    headers = ["task_id","task","task_priority","deadline","status"]
    with open("Stage 1/tasks.csv",mode='a',newline='',encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writerow({
            "task_id":id,
            "task":task_title,
            "task_priority":priority,
            "deadline":due_tate,
            "status":status       
        })
def load_data():
    # script_dir=os.path.dirname(os.path.abspath(__file__))
    # file_path = os.path.join(script_dir,"Stage 1","tasks.csv")
    retrieved_tasks=[]
    # if not os.path.exists(file_path):
    #     return retrieved_tasks
    with open(file="Stage 1/tasks.csv",mode='r',encoding="utf-8",) as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["task_id"]=int(row["task_id"])
            retrieved_tasks.append(dict(row))
    return retrieved_tasks
def save_all_to_csv(tasks):
    headers = ["task_id","task","task_priority","deadline","status"]
    with open("Stage 1/tasks.csv",mode='w',newline='',encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        for task in tasks:
            writer.writerow(task)
def has_match(pattern, text):
    # re.search looks across the entire string from start to finish
    return bool(re.search(pattern, text))
def date_check(task_date):
    day,month,year = map(int,task_date.split("-"))
    date1 = dt.date(year=year,month=month,day=day)
    now = dt.datetime.now().date()
    return date1>=now
def priority_handler(task_priority):
    return task_priority.strip().capitalize() in {"Low", "Medium", "High"}
class InvalidDateError(Exception):
    pass
class InvalidPriorityError(Exception):
    pass
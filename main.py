import db
from style import *

db.init_tables()

while True:
    print(lgreen + "\n=====MENU=====" + reset)
    print(lblue + "1. Add" + reset)
    print(lblue + "2. View" + reset)
    print(lblue + "3. Update" + reset)
    print(lblue + "4. Delete" + reset)
    print(lblue + "0. Exit" + reset)
    choice = input("Choice: ")
    match choice:
        case "1":
            title = input("Title: ")
            desc = input("Description: ")
            db.add_task(title, desc)
        case "2":
            db.view_tasks()
        case "3":
            task_id = input("ID: ")
            title = input("New title: ")
            desc = input("New description: ")
            db.update_task(task_id, title, desc)
        case "4":
            task_id = input("ID: ")
            db.delete_task(task_id)
        case "0":
            break
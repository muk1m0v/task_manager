import db
import user
from style import *

db.init_tables()

def show_menu():
    print(lgreen + "\n=====TASK MANAGER=====" + reset)
    print(lblue + "1. Add" + reset)
    print(lblue + "2. View" + reset)
    print(lblue + "3. Update" + reset)
    print(lblue + "4. Delete" + reset)
    print(lblue + "0. Exit" + reset)

while True:
    print(lgreen + "\n=====AUTH=====" + reset)
    print(lblue + "1. Login" + reset)
    print(lblue + "2. Register" + reset)
    print(lblue + "0. Exit" + reset)
    choice = input("Choice: ")
    match choice:
        case "1":
            full_name = input("Username: ")
            password = input("Password: ")
            if user.login(full_name, password):
                print(lgreen + f"Welcome, {full_name}!" + reset)
                while True:
                    show_menu()
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
            else:
                print(lred + "Invalid credentials!" + reset)
        case "2":
            full_name = input("Username: ")
            if user.user_exists(full_name):
                print(lred + "User already exists!" + reset)
            else:
                password = input("Password: ")
                user.register(full_name, password)
        case "0":
            break
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
import db
import auth
from style import *
import getpass

db.init_tables()

def task_menu():
    while True:
        print(lgreen + "\n=====TASK MANAGER=====" + reset)
        print(lblue + "1. Add" + reset)
        print(lblue + "2. View" + reset)
        print(lblue + "3. Update" + reset)
        print(lblue + "4. Delete" + reset)
        print(lblue + "0. Exit" + reset)
        choice = input("Choice: ")
        match choice:
            case "1":
                db.add_task(input("Title: "), input("Description: "))
            case "2":
                db.view_tasks()
            case "3":
                db.update_task(input("ID: "), input("New title: "), input("New description: "))
            case "4":
                db.delete_task(input("ID: "))
            case "0":
                break

def auth_menu():
    while True:
        print(lgreen + "\n=====AUTH=====" + reset)
        print(lblue + "1. Login" + reset)
        print(lblue + "2. Register" + reset)
        print(lblue + "0. Exit" + reset)
        choice = input("Choice: ")
        match choice:
            case "1":
                name = input("Username: ")
                if auth.login(name, getpass("Password: ")):
                    print(lgreen + f"Welcome, {name}!" + reset)
                    task_menu()
                else:
                    print(lred + "Invalid credentials!" + reset)
            case "2":
                name = input("Username: ")
                if auth.user_exists(name):
                    print(lred + "User already exists!" + reset)
                else:
                    auth.register(name, getpass("Password: "))
            case "0":
                break

auth_menu()
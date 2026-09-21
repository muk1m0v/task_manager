import psycopg
from os import getenv
from dotenv import load_dotenv
from style import *

load_dotenv()

def get_connection():
    try:
        conn = psycopg.connect(
            dbname=getenv('DB_NAME'),
            user=getenv('DB_USER'),
            password=getenv('DB_PASS'),
            host=getenv('DB_HOST'),
            port=getenv('DB_PORT')
        )

        return conn
    except Exception as err:
        print(lred + 'Connection Database Error',err, reset)

def init_tables():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS Tasks
        (
            task_id SERIAL PRIMARY KEY,
            title VARCHAR(200) NOT NULL,
            discaption TEXT DEFAULT NULL,
            created_date DATE DEFAULT CURRENT_DATE
        );
        ''')
        conn.commit()
        cur.close()

    except Exception as err:
        print(lred + 'Tables created error',err ,reset)

def add_task(title, desc):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Tasks (title, discaption) VALUES (%s, %s)", (title, desc))
    conn.commit()
    cur.close()
    conn.close()

def view_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Tasks")
    for row in cur.fetchall():
        print(f'ID: {int(row[0])} | Title: {row[1]} | Description: {row[2]} | Date: {row[3]}')
    cur.close()
    conn.close()

def update_task(task_id, title, desc):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE Tasks SET title=%s, discaption=%s WHERE task_id=%s", (title, desc, task_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Tasks WHERE task_id=%s", (task_id,))
    conn.commit()
    cur.close()
    conn.close()

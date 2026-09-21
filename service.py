from db import get_connection

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
        print(f'ID: {row[0]} | Title: {row[1]} | Description: {row[2]} | Date: {row[3]}')
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
import db

def register(full_name, password):
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Users (full_name, password) VALUES (%s, %s)", (full_name, password))
    conn.commit()
    cur.close()
    conn.close()

def login(full_name, password):
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, full_name FROM Users WHERE full_name=%s AND password=%s", (full_name, password))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

def user_exists(full_name):
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM Users WHERE full_name=%s", (full_name,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user
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
        CREATE TABLE IF NOT EXISTS Users
        (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL
        );
        ''')
        
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


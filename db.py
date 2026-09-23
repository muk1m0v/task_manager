import asyncpg
from os import getenv
from dotenv import load_dotenv
from style import red, green, reset

load_dotenv()


async def get_connection():
    try:
        conn = await asyncpg.connect(
            database=getenv("DB_NAME"),
            user=getenv("DB_USER"),
            password=getenv("DB_PASS"),
            host=getenv("DB_HOST"),
            port=int(getenv("DB_PORT")),
        )
        print(green + "Подключено" + reset)
        return conn
    except Exception as e:
        print(red + f"Ошибка подключения: {e}" + reset)
        raise


async def init_tables(conn):
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tables (
            id SERIAL PRIMARY KEY,
            number INTEGER UNIQUE NOT NULL,
            seats INTEGER DEFAULT 4
        );
        """
    )
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS categories (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL
        );
        """
    )
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS dishes (
            id SERIAL PRIMARY KEY,
            name VARCHAR(150) NOT NULL,
            price NUMERIC(10, 2) NOT NULL,
            category_id INTEGER REFERENCES categories(id) ON DELETE SET NULL
        );
        """
    )
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            table_id INTEGER REFERENCES tables(id) ON DELETE CASCADE,
            dish_id INTEGER REFERENCES dishes(id) ON DELETE CASCADE,
            quantity INTEGER DEFAULT 1,
            status VARCHAR(20) DEFAULT 'new'
        );
        """
    )
    print(green + "Таблицы готовы: tables, categories, dishes, orders" + reset)

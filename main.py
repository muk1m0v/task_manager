import asyncio
from dotenv import load_dotenv
from db import get_connection, init_tables
from service import main_menu
from style import red, reset

load_dotenv()


async def main():
    conn = await get_connection()
    try:
        await init_tables(conn)
        await main_menu(conn)
    finally:
        await conn.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(red + str(e) + reset)

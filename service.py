import asyncio
from style import red, green, cyan, reset
import tables as tbl
import categories as cat
import dishes as dsh
import orders as ord


async def ainput(prompt):
    return await asyncio.to_thread(input, prompt)


async def tables_menu(conn):
    while True:
        print("\nСтолы: 1-показать 2-добавить 3-найти 4-изменить 5-удалить 0-назад")
        ch = (await ainput("Выбери: ")).strip()
        if ch == "1":
            for r in await tbl.get_all(conn):
                print(f"{r['id']}. Стол {r['number']} - мест: {r['seats']}")
        elif ch == "2":
            number = int(await ainput("Номер стола: "))
            seats = int(await ainput("Мест: ") or 4)
            nid = await tbl.add(conn, number, seats)
            print(green + f"Добавлено: {nid}" + reset)
        elif ch == "3":
            print(await tbl.get_one(conn, int(await ainput("ID: "))))
        elif ch == "4":
            tid = int(await ainput("ID: "))
            number = int(await ainput("Новый номер: "))
            seats = int(await ainput("Мест: "))
            print(await tbl.update(conn, tid, number, seats))
        elif ch == "5":
            print(await tbl.delete(conn, int(await ainput("ID: "))))
        elif ch == "0":
            break


async def categories_menu(conn):
    while True:
        print("\nКатегории: 1-показать 2-добавить 3-найти 4-изменить 5-удалить 0-назад")
        ch = (await ainput("Выбери: ")).strip()
        if ch == "1":
            for r in await cat.get_all(conn):
                print(f"{r['id']}. {r['name']}")
        elif ch == "2":
            nid = await cat.add(conn, (await ainput("Название: ")).strip())
            print(green + f"Добавлено: {nid}" + reset)
        elif ch == "3":
            print(await cat.get_one(conn, int(await ainput("ID: "))))
        elif ch == "4":
            cid = int(await ainput("ID: "))
            print(await cat.update(conn, cid, (await ainput("Новое название: ")).strip()))
        elif ch == "5":
            print(await cat.delete(conn, int(await ainput("ID: "))))
        elif ch == "0":
            break


async def dishes_menu(conn):
    while True:
        print("\nБлюда: 1-показать 2-добавить 3-найти 4-изменить 5-удалить 0-назад")
        ch = (await ainput("Выбери: ")).strip()
        if ch == "1":
            for r in await dsh.get_all(conn):
                print(f"{r['id']}. {r['name']} - {r['price']} ({r['category']})")
        elif ch == "2":
            name = (await ainput("Название: ")).strip()
            price = float(await ainput("Цена: "))
            category_id = int(await ainput("ID категории: "))
            nid = await dsh.add(conn, name, price, category_id)
            print(green + f"Добавлено: {nid}" + reset)
        elif ch == "3":
            print(await dsh.get_one(conn, int(await ainput("ID: "))))
        elif ch == "4":
            did = int(await ainput("ID: "))
            name = (await ainput("Название: ")).strip()
            price = float(await ainput("Цена: "))
            category_id = int(await ainput("ID категории: "))
            print(await dsh.update(conn, did, name, price, category_id))
        elif ch == "5":
            print(await dsh.delete(conn, int(await ainput("ID: "))))
        elif ch == "0":
            break


async def orders_menu(conn):
    while True:
        print("\nЗаказы: 1-показать 2-заказать 3-найти 4-изменить 5-удалить 0-назад")
        ch = (await ainput("Выбери: ")).strip()
        if ch == "1":
            for r in await ord.get_all(conn):
                print(f"{r['id']}. Стол {r['table_number']} - {r['dish']} x{r['quantity']} = {r['total']} [{r['status']}]")
        elif ch == "2":
            table_id = int(await ainput("ID стола: "))
            dish_id = int(await ainput("ID блюда: "))
            qty = int(await ainput("Количество: ") or 1)
            nid = await ord.add(conn, table_id, dish_id, qty)
            print(green + f"Заказ {nid} принят" + reset)
        elif ch == "3":
            print(await ord.get_one(conn, int(await ainput("ID: "))))
        elif ch == "4":
            oid = int(await ainput("ID: "))
            table_id = int(await ainput("ID стола: "))
            dish_id = int(await ainput("ID блюда: "))
            qty = int(await ainput("Количество: "))
            status = (await ainput("Статус: ")).strip()
            print(await ord.update(conn, oid, table_id, dish_id, qty, status))
        elif ch == "5":
            print(await ord.delete(conn, int(await ainput("ID: "))))
        elif ch == "0":
            break


async def main_menu(conn):
    while True:
        print(cyan + "====MENU====\n1. Столы \n2. Категории \n3. Блюда \n4. Заказы \n0. Выход" + reset)
        ch = (await ainput("Выбери: ")).strip()
        if ch == "1":
            await tables_menu(conn)
        elif ch == "2":
            await categories_menu(conn)
        elif ch == "3":
            await dishes_menu(conn)
        elif ch == "4":
            await orders_menu(conn)
        elif ch == "0":
            print("Пока!")
            break
        else:
            print(red + "Нет такого пункта" + reset)

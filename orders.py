async def add(conn, table_id, dish_id, quantity=1):
    row = await conn.fetchrow(
        "INSERT INTO orders (table_id, dish_id, quantity) VALUES ($1, $2, $3) RETURNING id",
        table_id,
        dish_id,
        quantity,
    )
    return row["id"]


async def get_all(conn):
    rows = await conn.fetch(
        """
        SELECT o.id, t.number AS table_number, d.name AS dish,
               o.quantity, o.status, (d.price * o.quantity) AS total
        FROM orders o
        JOIN tables t ON t.id = o.table_id
        JOIN dishes d ON d.id = o.dish_id
        ORDER BY o.id
        """
    )
    return [dict(r) for r in rows]


async def get_one(conn, oid):
    row = await conn.fetchrow("SELECT * FROM orders WHERE id = $1", oid)
    return dict(row) if row else None


async def update(conn, oid, table_id, dish_id, quantity, status):
    return await conn.execute(
        "UPDATE orders SET table_id = $1, dish_id = $2, quantity = $3, status = $4 WHERE id = $5",
        table_id,
        dish_id,
        quantity,
        status,
        oid,
    )


async def delete(conn, oid):
    return await conn.execute("DELETE FROM orders WHERE id = $1", oid)

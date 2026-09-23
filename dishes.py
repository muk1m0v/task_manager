async def add(conn, name, price, category_id):
    row = await conn.fetchrow(
        "INSERT INTO dishes (name, price, category_id) VALUES ($1, $2, $3) RETURNING id",
        name,
        price,
        category_id,
    )
    return row["id"]


async def get_all(conn):
    rows = await conn.fetch(
        """
        SELECT d.id, d.name, d.price, c.name AS category
        FROM dishes d
        LEFT JOIN categories c ON c.id = d.category_id
        ORDER BY d.id
        """
    )
    return [dict(r) for r in rows]


async def get_one(conn, did):
    row = await conn.fetchrow("SELECT * FROM dishes WHERE id = $1", did)
    return dict(row) if row else None


async def update(conn, did, name, price, category_id):
    return await conn.execute(
        "UPDATE dishes SET name = $1, price = $2, category_id = $3 WHERE id = $4",
        name,
        price,
        category_id,
        did,
    )


async def delete(conn, did):
    return await conn.execute("DELETE FROM dishes WHERE id = $1", did)

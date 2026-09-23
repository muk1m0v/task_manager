async def add(conn, name):
    row = await conn.fetchrow(
        "INSERT INTO categories (name) VALUES ($1) RETURNING id",
        name,
    )
    return row["id"]


async def get_all(conn):
    rows = await conn.fetch("SELECT * FROM categories ORDER BY id")
    return [dict(r) for r in rows]


async def get_one(conn, cid):
    row = await conn.fetchrow("SELECT * FROM categories WHERE id = $1", cid)
    return dict(row) if row else None


async def update(conn, cid, name):
    return await conn.execute(
        "UPDATE categories SET name = $1 WHERE id = $2", name, cid
    )


async def delete(conn, cid):
    return await conn.execute("DELETE FROM categories WHERE id = $1", cid)

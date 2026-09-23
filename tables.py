async def add(conn, number, seats=4):
    row = await conn.fetchrow(
        "INSERT INTO tables (number, seats) VALUES ($1, $2) RETURNING id",
        number,
        seats,
    )
    return row["id"]


async def get_all(conn):
    rows = await conn.fetch("SELECT * FROM tables ORDER BY number")
    return [dict(r) for r in rows]


async def get_one(conn, tid):
    row = await conn.fetchrow("SELECT * FROM tables WHERE id = $1", tid)
    return dict(row) if row else None


async def update(conn, tid, number, seats):
    return await conn.execute(
        "UPDATE tables SET number = $1, seats = $2 WHERE id = $3",
        number,
        seats,
        tid,
    )


async def delete(conn, tid):
    return await conn.execute("DELETE FROM tables WHERE id = $1", tid)

import sqlite3
from datetime import datetime

db = sqlite3.connect('profile.db')
cur = db.cursor()


async def connect():
    query = """
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER NOT NULL UNIQUE,
            subscribe TEXT NULL,
            subscribe_start TEXT NULL,
            subscribe_finish TEXT NULL,
            user_id_wallet TEXT NULL
        )
    """
    cur.execute(query)
    db.commit()


async def add_user(user_id):
    query = "INSERT INTO user(user_id) VALUES (?)"
    cur.execute(query, (user_id,))
    db.commit()


async def status(user_id):
    stat = cur.execute("""SELECT * FROM user WHERE user_id=?""", (user_id,)).fetchone()
    return stat


async def days_between_dates(date1: str, date2: str) -> int:
    dt1 = datetime.strptime(date1, "%d.%m.%Y")
    dt2 = datetime.strptime(date2, "%d.%m.%Y")
    delta = dt2 - dt1
    return delta.days


async def subscription(user_id: int, subscribe: str, subscribe_start: str, subscribe_finish: str):
    check_query = "SELECT user_id FROM user WHERE user_id = ?"
    cur.execute(check_query, (user_id,))
    result = cur.fetchone()
    if result is None:
        await add_user(user_id)
    update_query = """
            INSERT INTO user (user_id, subscribe, subscribe_start, subscribe_finish)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
            subscribe = excluded.subscribe,
            subscribe_start = excluded.subscribe_start,
            subscribe_finish = excluded.subscribe_finish
        """
    cur.execute(update_query, (user_id, subscribe, subscribe_start, subscribe_finish))
    db.commit()
    num_days = await days_between_dates(subscribe_start, subscribe_finish)
    return num_days


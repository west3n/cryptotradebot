from datetime import datetime
import mysql.connector
from decouple import config

db = mysql.connector.connect(
    host=config('DB_HOST'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
    database=config('DB_NAME'),
    port=config('DB_PORT')
)

cur = db.cursor()


async def connect_main():
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
    query = "INSERT INTO user(user_id) VALUES (%s)"
    cur.execute(query, (user_id,))
    db.commit()


async def status(user_id):
    cur = db.cursor()
    query = """SELECT * FROM user WHERE user_id=%s"""
    cur.execute(query, (user_id,))
    result = cur.fetchone()
    cur.close()
    return result


async def days_between_dates(date1: str, date2: str) -> int:
    dt1 = datetime.strptime(date1, "%d.%m.%Y")
    dt2 = datetime.strptime(date2, "%d.%m.%Y")
    delta = dt2 - dt1
    return delta.days


async def subscription(user_id: int, subscribe: str, subscribe_start: str, subscribe_finish: str):
    check_query = "SELECT user_id FROM user WHERE user_id = %s"
    cur.execute(check_query, (user_id,))
    result = cur.fetchone()
    if result is None:
        await add_user(user_id)
    update_query = """
            INSERT INTO user (user_id, subscribe, subscribe_start, subscribe_finish)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            subscribe = VALUES(subscribe),
            subscribe_start = VALUES(subscribe_start),
            subscribe_finish = VALUES(subscribe_finish)
        """
    cur.execute(update_query, (user_id, subscribe, subscribe_start, subscribe_finish))
    db.commit()
    num_days = await days_between_dates(subscribe_start, subscribe_finish)
    return num_days

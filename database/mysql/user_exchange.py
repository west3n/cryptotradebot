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


async def connect_exchange():
    query = """
        CREATE TABLE IF NOT EXISTS user_exchange (
            user_id INT(11) NOT NULL,
            exc VARCHAR(150),
            api_key VARCHAR(150),
            api_secret VARCHAR(150),
            CONSTRAINT unique_user_exc UNIQUE (user_id, exc)
        )
    """
    cur.execute(query)
    db.commit()


async def add_exchange(user_id, data):
    query = "INSERT INTO user_exchange(user_id, exc, api_key, api_secret) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (user_id, data.get('exc'), data.get('api_key'), data.get('api_secret'),))
    db.commit()


async def status(user_id):
    query = "SELECT * FROM user_exchange WHERE user_id=%s"
    cur.execute(query, (user_id,))
    stat = cur.fetchall()
    return stat


async def exc_api(user_id):
    query = "SELECT exc, api_key FROM user_exchange WHERE user_id=%s"
    cur.execute(query, (user_id,))
    stat = cur.fetchall()
    return stat


async def get_api(user_id, exc):
    query = "SELECT api_key, api_secret FROM user_exchange WHERE user_id=%s AND exc=%s"
    cur.execute(query, (user_id, exc,))
    stat = cur.fetchone()
    return stat


async def delete_api(user_id, exc):
    query = "DELETE FROM user_exchange WHERE user_id=%s AND exc=%s"
    cur.execute(query, (user_id, exc,))
    db.commit()


async def api_key_status(user_id):
    cur = db.cursor()
    query = """SELECT * FROM user_exchange WHERE user_id=%s"""
    cur.execute(query, (user_id,))
    result = cur.fetchone()
    cur.close()
    return result

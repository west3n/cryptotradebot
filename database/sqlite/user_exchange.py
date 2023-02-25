import sqlite3

db = sqlite3.connect('profile.db')
cur = db.cursor()


async def connect_exchange():
    query = """
        CREATE TABLE IF NOT EXISTS user_exchange (
            user_id INTEGER NOT NULL,
            exc TEXT NULL,
            api_key TEXT NULL,
            api_secret TEXT NULL,
            CONSTRAINT unique_user_exc UNIQUE (user_id, exc)
        )
    """
    cur.execute(query)
    db.commit()


async def add_exchange(user_id, data):
    query = "INSERT INTO user_exchange(user_id, exc, api_key, api_secret) VALUES (?, ?, ?, ?)"
    cur.execute(query, (user_id, data.get('exc'), data.get('api_key'), data.get('api_secret'),))
    db.commit()


async def status(user_id):
    stat = cur.execute("""SELECT * FROM user_exchange WHERE user_id=?""", (user_id,)).fetchall()
    return stat


async def exc_api(user_id):
    stat = cur.execute("""SELECT exc, api_key FROM user_exchange WHERE user_id=?""", (user_id,)).fetchall()
    return stat


async def get_api(user_id, exc):
    stat = cur.execute("""SELECT api_key, api_secret FROM user_exchange WHERE user_id=? AND exc=?""",
                       (user_id, exc,)).fetchone()
    return stat


async def delete_api(user_id, exc):
    cur.execute("""DELETE FROM user_exchange WHERE user_id=? AND exc=?""", (user_id, exc,))
    db.commit()

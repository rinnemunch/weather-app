import sqlite3


def init_db():
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_city(city):
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("INSERT INTO history (city) VALUES (?)", (city,))
    conn.commit()
    conn.close()


def get_recent_cities(limit=5):
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("SELECT city FROM history ORDER BY id DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return [row[0] for row in rows]


def clear_history():
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("DELETE FROM history")
    conn.commit()
    conn.close()

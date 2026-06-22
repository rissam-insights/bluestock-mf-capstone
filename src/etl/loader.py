import sqlite3
from pathlib import Path

DB_NAME = "nifty100.db"

conn = sqlite3.connect(DB_NAME)

cursor = conn.cursor()

schema_path = Path("db/schema.sql")

with open(schema_path, "r", encoding="utf-8") as f:
    schema = f.read()

cursor.executescript(schema)

conn.commit()

print("Database schema created successfully!")

conn.close()
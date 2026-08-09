import sqlite3
import os

# Project root folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database path
DB_PATH = os.path.join(BASE_DIR, "database", "online_exam.db")


def get_connection():
    try:
        print(f"\nDatabase Path: {DB_PATH}")

        connection = sqlite3.connect(DB_PATH, timeout=10)

        # Prevent database locking
        connection.execute("PRAGMA journal_mode=WAL")
        connection.execute("PRAGMA busy_timeout=10000")

        return connection

    except Exception as e:
        print("Database Connection Error:", e)
        return None
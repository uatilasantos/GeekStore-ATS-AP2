import sqlite3
import os

DB_PATH = os.getenv("DB_PATH", "geekstore.db")


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            nome TEXT PRIMARY KEY,
            preco REAL,
            estoque INTEGER
        )
    """)

    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM produtos")

    if cursor.fetchone()[0] == 0:
        conn.execute("""
            INSERT INTO produtos (nome, preco, estoque)
            VALUES ('teclado', 200.0, 10)
        """)

        conn.execute("""
            INSERT INTO produtos (nome, preco, estoque)
            VALUES ('mouse', 100.0, 5)
        """)

    conn.commit()
    conn.close()
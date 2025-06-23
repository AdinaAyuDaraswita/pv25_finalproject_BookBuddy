import sqlite3

def create_connection():
    conn = sqlite3.connect("bookbuddy.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Tabel Buku
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            author TEXT NOT NULL,
            date DATE NOT NULL,
            status TEXT CHECK(status IN ('Tersedia', 'Dipinjam')) NOT NULL
        )
    """)

    # Tabel Anggota
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            join_date DATE NOT NULL
        )
    """)

    # Tabel Peminjaman
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrowings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            borrower TEXT NOT NULL,
            borrow_date DATE NOT NULL,
            due_date DATE NOT NULL,
            status TEXT CHECK(status IN ('Dipinjam', 'Dikembalikan')) NOT NULL
        )
    """)

    conn.commit()
    conn.close()

import sqlite3

DATABASE = "students.db"

def connect():
    return sqlite3.connect(DATABASE)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT,
        email TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_student(name, age, course, email):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
        (name, age, course, email)
    )

    conn.commit()
    conn.close()

def get_students():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()
    return rows

def search_student(name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    rows = cursor.fetchall()
    conn.close()
    return rows

def update_student(id, name, age, course, email):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET name=?, age=?, course=?, email=?
        WHERE id=?
    """, (name, age, course, email, id))

    conn.commit()
    conn.close()

def delete_student(id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()
    conn.close()
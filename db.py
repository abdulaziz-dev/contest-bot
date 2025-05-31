import sqlite3

def init_db():
    conn = sqlite3.connect("votes.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        contact_shared BOOLEAN DEFAULT 0
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        subject_id INTEGER NOT NULL,
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS votes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    )
    """)

    conn.commit()
    conn.close()

def get_subjects():
    conn = sqlite3.connect("votes.db")
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM subjects ORDER BY name")
    results = cur.fetchall()
    conn.close()
    return results

def get_teachers_by_subject(subject_id):
    conn = sqlite3.connect("votes.db")
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM teachers WHERE subject_id = ?", (subject_id,))
    results = cur.fetchall()
    conn.close()
    return results

def add_vote(user_id, teacher_id):
    conn = sqlite3.connect("votes.db")
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO votes (user_id, teacher_id) VALUES (?, ?)", (user_id, teacher_id))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_vote_results():
    conn = sqlite3.connect("votes.db")
    cur = conn.cursor()
    cur.execute("""
    SELECT t.name, COUNT(v.id) as vote_count
    FROM votes v
    JOIN teachers t ON v.teacher_id = t.id
    GROUP BY v.teacher_id
    ORDER BY vote_count DESC
    """)
    results = cur.fetchall()
    conn.close()
    return results

def has_shared_contact(user_id):
    conn = sqlite3.connect("votes.db")
    cur = conn.cursor()
    cur.execute("SELECT contact_shared FROM users WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    conn.close()
    return result is not None and result[0] == 1

def mark_contact_shared(user_id):
    conn = sqlite3.connect("votes.db")
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO users (user_id, contact_shared) VALUES (?, 1)", (user_id,))
    conn.commit()
    conn.close()
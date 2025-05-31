import sqlite3

conn = sqlite3.connect("votes.db")
cur = conn.cursor()

# Add subjects
subjects = ["Matematika", "Biologiya", "Tarix"]
for name in subjects:
    cur.execute("INSERT OR IGNORE INTO subjects (name) VALUES (?)", (name,))
conn.commit()

# Get subject IDs
cur.execute("SELECT id, name FROM subjects")
subject_map = {name: id for id, name in cur.fetchall()}

# Add teachers
cur.execute("INSERT INTO teachers (name, subject_id) VALUES (?, ?)", ("Aliyev A.", subject_map["Matematika"]))
cur.execute("INSERT INTO teachers (name, subject_id) VALUES (?, ?)", ("Karimova B.", subject_map["Matematika"]))
cur.execute("INSERT INTO teachers (name, subject_id) VALUES (?, ?)", ("Tursunov C.", subject_map["Tarix"]))
conn.commit()
conn.close()

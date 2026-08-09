import sqlite3


conn = sqlite3.connect("database/online_exam.db")

cursor = conn.cursor()


cursor.execute("""
ALTER TABLE exam
ADD COLUMN duration INTEGER DEFAULT 10
""")


conn.commit()

conn.close()


print("Duration Column Added Successfully")
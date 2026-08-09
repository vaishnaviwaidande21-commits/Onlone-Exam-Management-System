import sqlite3

conn = sqlite3.connect("database/online_exam.db")
cursor = conn.cursor()

# Delete all questions
cursor.execute("DELETE FROM question")

# Reset Auto Increment
cursor.execute("DELETE FROM sqlite_sequence WHERE name='question'")

conn.commit()
conn.close()

print("=" * 50)
print("Question table reset successfully!")
print("Question IDs will now start from 1.")
print("=" * 50)
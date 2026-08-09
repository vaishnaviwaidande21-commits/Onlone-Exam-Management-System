import sqlite3


conn = sqlite3.connect("database/online_exam.db")
cursor = conn.cursor()



def add_column(table, column, datatype):

    try:

        cursor.execute(
            f"ALTER TABLE {table} ADD COLUMN {column} {datatype}"
        )

        print(f"{column} added successfully")


    except sqlite3.OperationalError:

        print(f"{column} already exists")



# Question Table Update

add_column("question", "subject", "TEXT")
add_column("question", "difficulty", "TEXT")
add_column("question", "topic", "TEXT")
add_column("question", "question_type", "TEXT")



conn.commit()
conn.close()


print("=" * 50)
print("Database updated successfully")
print("=" * 50)

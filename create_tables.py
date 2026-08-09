import sqlite3
import os


# Database path
os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/online_exam.db")
cursor = conn.cursor()


# ===========================
# Admin Table
# ===========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin(
    admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")


# Default Admin
cursor.execute("""
INSERT OR IGNORE INTO admin(username, password)
VALUES('admin','admin123')
""")


# ===========================
# Student Table
# ===========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    course TEXT
)
""")


# ===========================
# Teacher Table
# ===========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS teacher(
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    subject TEXT
)
""")


# ===========================
# Exam Table
# ===========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS exam(
    exam_id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_name TEXT,
    subject TEXT,
    teacher_id INTEGER,

    FOREIGN KEY(teacher_id)
    REFERENCES teacher(teacher_id)
)
""")


# ===========================
# Question Table
# ===========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS question(

    question_id INTEGER PRIMARY KEY AUTOINCREMENT,

    exam_id INTEGER,

    topic TEXT,

    question_text TEXT,

    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,

    correct_answer TEXT,

    subject TEXT,

    difficulty TEXT,

    question_type TEXT,


    FOREIGN KEY(exam_id)
    REFERENCES exam(exam_id)

)
""")


# ===========================
# Result Table
# ===========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS result(

    result_id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id INTEGER,

    exam_id INTEGER,

    total_questions INTEGER,

    correct_answers INTEGER,

    wrong_answers INTEGER,

    percentage REAL,

    grade TEXT,

    analysis TEXT,

    date TEXT,


    FOREIGN KEY(student_id)
    REFERENCES student(student_id),


    FOREIGN KEY(exam_id)
    REFERENCES exam(exam_id)

)
""")


# ===========================
# Student Answer Table
# ===========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS student_answer(

    answer_id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id INTEGER,

    exam_id INTEGER,

    question_id INTEGER,

    selected_answer TEXT,

    correct_answer TEXT,


    FOREIGN KEY(student_id)
    REFERENCES student(student_id),


    FOREIGN KEY(exam_id)
    REFERENCES exam(exam_id),


    FOREIGN KEY(question_id)
    REFERENCES question(question_id)

)
""")


conn.commit()
conn.close()


print("="*50)
print("Database Tables Created Successfully")
print("="*50)
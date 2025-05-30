import sqlite3

def get_connection(path):
    try:
        conn = sqlite3.connect(f"{path}")
        return conn
    except sqlite3.Error as e:
        print(f"Error: {e}")

def create_test_table(conn:sqlite3.Connection):
    cur = conn.cursor()
    studentsTable = '''
                CREATE TABLE students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                age INTEGER,
                class_id INTEGER NOT NULL,
                FOREIGN KEY (class_id) REFERENCES classes(id));'''
    classesTable = '''
                CREATE TABLE classes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL UNIQUE,
                teacher_id INTEGER NOT NULL,
                FOREIGN KEY (teacher_id) REFERENCES teachers(id));'''
    teachersTable = '''
                CREATE TABLE teachers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL);'''
    try:
        cur.execute(studentsTable)
        cur.execute(classesTable)
        cur.execute(teachersTable)
    except sqlite3.Error as e:
        print(f"ERROR : {e}")


def insert_test_data(conn:sqlite3.Connection):
    cur = conn.cursor()
    studentsData = [
        ("An Nguyễn", 15, 1),
        ("Bình Trần", 16, 1),
        ("Cường Lê", 16, 2),
        ("Dương Phạm", 17, 2),
        ("Emi Hoàng", 17, 3),
        ("Hà Nguyễn", 18, 3),
        ("Hùng Trần", 16, 4),
        ("Lan Phạm", 17, 4),
        ("Minh Lê", 18, 5),
        ("Oanh Hoàng", 18, 5)
    ]
    classesData = [
        ("Lớp 10A", 1),
        ("Lớp 10B", 2),
        ("Lớp 11A", 3),
        ("Lớp 11B", 4),
        ("Lớp 12A", 5)
    ]
    teachersData = [
        ("Nguyễn Văn A",),
        ("Trần Thị B",),
        ("Lê Văn C",),
        ("Phạm Thị D",),
        ("Hoàng Văn E",)
    ]
    try:
        cur.executemany("INSERT INTO students (name, age, class_id) VALUES (?,?,?)", studentsData)
        cur.executemany("INSERT INTO classes (name,teacher_id) VALUES (?,?)", classesData)
        cur.executemany("INSERT INTO teachers (name) VALUES (?)", teachersData)
    except sqlite3.Error as e:
        print(f"ERROR : {e}")
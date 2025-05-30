import sqlite3

#them teacher
def add_teacher(cur, data):
    try:
        cur.execute("insert into teachers values (?, ?)", data)
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

def add_supteacher(cur, name: str):
    try:
        cur.execute("insert into teachers (name) values  (?)", (name,))
    except sqlite3.IntegrityError as e:
        print(f"Error integrity: {e}")
    except sqlite3.Error as e:
        print(f"Error: {e}")

#sua teacher
def update_teacher(cur, id: int, name: str):
    try:
        cur.execute("update teachers set name = ? where id = ?", (name,id))
    except sqlite3.IntegrityError as e:
        print(f"Error integrity: {e}")
    except sqlite3.Error as e:
        print(f"Error: {e}")

#delete teacher
def delete_teacher(cur, id: int):
    try:
        cur.execute("delete from teachers where id = ?", (id,))
    except sqlite3.IntegrityError as e:
        print(f"Error integrity: {e}")
    except sqlite3.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    con = sqlite3.connect('testgpt.db')
    cur = con.cursor()
    # data = [
    #     ('6', 'Huy'),
    #     ('7', 'Nhut'),
    #     ('8', 'Dong'),
    #     ('9', 'Phong'),
    #     ('10', 'Khanh')
    # ]
    # for item in data:
    #     add_teacher(cur, item)
    # con.commit()

    # add_supteacher(cur, 'Huong')

    update_teacher(cur, 3, 'Tuan')
    delete_teacher(cur, 3)
    cur.execute("select * from teachers")
    for row in cur.fetchall():
        print(row)
    print("----------------------")


    con.rollback()
    cur.execute("select * from teachers")
    for row in cur.fetchall():
        print(row)

    
    #con.commit()

import testDatabase
import sqlite3
import BT
if __name__ == "__main__":
    conn = testDatabase.get_connection("testgpt.db")
    cur = conn.cursor()
    if conn:
        testDatabase.create_test_table(conn)
        testDatabase.insert_test_data(conn)
        conn.commit()
        conn.close()
        print("Test database created successfully.")


        # BT.update_teacher(cur, 3, 'Tuan')
        # BT.delete_teacher(cur, 3)
        # cur.execute("select * from teachers")
        # for row in cur.fetchall():
        #     print(row)
        # print("----------------------")


        # conn.rollback()
        # cur.execute("select * from teachers")
        # for row in cur.fetchall():
        #     print(row)

    
    #con.commit()
    else:
        print("Failed to create test database.")
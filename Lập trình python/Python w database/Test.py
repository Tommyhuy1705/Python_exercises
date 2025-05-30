import sqlite3

db_path = 'test.db'
con = sqlite3.connect('test.db')
cur = con.cursor()


data = [
    (70, 'HCM'),
    (50, 'DA NANG'),
    (90, 'HUE'),
    (10, 'HA NOI'),
    (20, 'CAN THO'),
    (30, 'NHA TRANG'),
    (40, 'VUNG TAU'),
    (70000, 'HCM'),
    (55000, 'DA NANG')]

# cur.executemany('INSERT INTO THANH_PHO VALUES (?, ?)', data)
# con.commit()

#delete data
# cur.execute('DELETE FROM THANH_PHO WHERE MATP = 70')
# cur.execute('DELETE FROM THANH_PHO WHERE MATP = 50')
# con.commit()

#update data
cur.execute('UPDATE THANH_PHO SET MATP = 50 WHERE MATP = 100')
con.commit()

cur.execute('SELECT * FROM THANH_PHO')
for row in cur.fetchall():
    print(row)
print('\n')

#select top in SQLITE3 --> LIMIT
cur.execute('SELECT * FROM THANH_PHO ORDER BY MATP ASC LIMIT 3')
for row in cur.fetchall():
    print(row)
print('\n')

cur.execute('SELECT * FROM THANH_PHO ORDER BY MATP DESC LIMIT 3')
for row in cur.fetchall():
    print(row)
print('\n')



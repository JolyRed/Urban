import sqlite3
import random

connect = sqlite3.connect('not_telegram.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL               
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS ind_balance ON Users (balance)")

#for i in range(1,11):
#    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)", 
#                  (f'User{i}', f'example{i}@gmail.com', random.randint(10, 70), random.randint(100, 1000)))

cursor.execute(" DELETE FROM Users WHERE id = 6 ")
cursor.execute(" SELECT COUNT(*) FROM Users ")
cursor.execute(" SELECT SUM(balance) FROM Users ")
cursor.execute(" SELECT AVG(balance) FROM Users ")
total1 = cursor.fetchone()[0]
print(round(total1, 1))
connect.commit()
connect.close()
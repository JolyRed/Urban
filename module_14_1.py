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

cursor.execute(" UPDATE Users SET balance = ? WHERE username = ?", (500, 'User1'))
cursor.execute(" UPDATE Users SET balance = ? WHERE (id % 2) = 0", (500, ))
cursor.execute(" DELETE FROM Users WHERE (id % 3) = 0")
cursor.execute(" SELECT  username, age, email, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(user)

connect.commit()
connect.close()
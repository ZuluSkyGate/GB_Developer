import sqlite3 as sl
from easygui import *

def select_all():
    cur.execute("SELECT * FROM users;")
    return cur.fetchall()

def add_values():
    cur.execute("INSERT INTO users VALUES (1,'Ваня','Петров');")
    cur.execute("INSERT INTO users VALUES (2,'Сергей','Сергеев');")

def select_ivan():
    cur.execute("SELECT * FROM users WHERE name = 'Ваня';")
    return cur.fetchall()

conn = sl.connect("test_evening.db")

cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS users
            (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT
            );
            """)

choice = choicebox("Выберите запрос", "Главная форма", 
                   ['Все записи', "Только Ваня"])
# add_values()

if choice == "Все записи":
    msg = str(select_all())
    msgbox(msg, "Результат запроса")
if choice == "Только Ваня":
    msg = str(select_ivan())
    msgbox(msg, "Результат запроса")


conn.commit()
conn.close()

phonebook = {"дядя Ваня": {'phones': [1212121,5555555],
                           'email': '777@mail.com', 'birthday': '10.10.1990'},
             "дядя Вася": {'phones': [888888]}                         
            }

print(phonebook['дядя Ваня'])
print(phonebook['дядя Ваня'] ['phones'])
print(phonebook['дядя Ваня'] ['phones'] [0])
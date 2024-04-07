from easygui import *
import sqlite3 as sq


with sq.connect("tel_spr_data.db") as con:
    cur = con.cursor()
    cur.execute("""
    """)

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    sex INTEGER,
    home_number INTEGER,
    work_number INTEGER
)""")


msgbox("Телефонный справочник v. 1.0", "Телефонный справочник", ok_button = "Старт")
msg = "Выберите Ваше действие"
title = "Действия"
choises = ['просмотреть', 'сохраненить', 'импортировать', 'найти', 'удалить', 'измененить']
choice = choicebox(msg, title, choises)



elif command=="a":
  cursor.execute ("SELECT * FROM notes ORDER BY id ASC")
  rows = cursor.fetchall ()
  for row in rows:
      print "n   %s %s [%s]" % (row[0], row[1], row[2])
  print "n   Number of records: %d" % cursor.rowcount

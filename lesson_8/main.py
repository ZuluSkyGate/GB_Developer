# import sqlite3 as sl
# from easygui import *


# def select_all():
#     cur.execute("SELECT * FROM users;")
#     return cur.fetchall()

# def add_values():
#     cur.execute("INSERT INTO users VALUES (1,'Ваня','Петров');")
#     cur.execute("INSERT INTO users VALUES (2,'Сергей','Сергеев');")

# def select_ivan():
#     cur.execute("SELECT * FROM users WHERE name = 'Ваня';")
#     return cur.fetchall()



# # создаем подключение к БД
# conn = sl.connect('lesson_7.db')

# # создаем курсор - объект для выполнения SQL
# cur = conn.cursor()

# # создали SQL запрос и выполнили
# cur.execute("""
#             CREATE TABLE IF NOT EXISTS users
#             (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             surname TEXT
#             );
#             """)

# # add_values()


# choice = choicebox("Выберите запрос", "Главная форма", 
#                    ['Все записи', "Только Ваня"])


# if choice == "Все записи":
#     msg = str(select_all())
#     msgbox(msg, "Результат запроса")
# elif choice == "Только Ваня":
#     msg = str(select_ivan())
#     msgbox(msg, "Результат запроса")



# # print(select_ivan())

# conn.commit()


# Задача №49. Решение в группах Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)

# 1. прога запускается, пробует подключиться к файлу
# 2. если файл есть то загружаем данные в коллекцию
# 3. если файла нет то можно подгрузить набор данных по умолчанию
# 4. внутри постоянно идет цикл While True , постоянно запрашивается некая команда
# 5. идет обработка этой команды 
# 6. новая итерация цикла
# 7. если стоп слово то выходим из цикла
# 8. автоматическое сохранение в файл

# phonebook = {
#     "дядя Ваня": { 'phones': [1231654,45646644], 
#                   'birthday': '01.01.1960', 
#                   'email': "vanya@mail.ru" },
#     "дядя Вася": {'phones' : [12121244444]}
# }

# print(phonebook['дядя Ваня'])
# print(phonebook['дядя Ваня'] ['phones'])

# print(phonebook['дядя Ваня'] ['phones'][-1])

import json



def save():
    with open ('telephonBook.json','a', encoding="utf-8") as phones:
        phones.write(json.dumps(phonebook, ensure_ascii=False))
    print("Контак добавлен")

def save_phonebook(phonebook):
    with open('phonebook.txt', 'w', encoding = 'utf-8') as data:
        for item in phonebook.items():  
            string = str(item)
            data.writelines(string)

def load():
    try:
        with open ('telephonBook.json','r', encoding="utf-8") as phones:
            phonebook = json.load(phones)
    except:
        phonebook = {
    "Служба спасения": { 'phones': [1231654,45646644], 
                      'birthday': '01.01.1960', 
                     'email': "vanya@mail.ru" },
    "Служба поддержки": {'phones' : [12121244444]} 
    }
    return phonebook

def find_number(name):
    return phonebook[name]

# подгуржаются файлы с телефона
phonebook = load()

while True:
    print('Что вы хотите сделать?')
    user_choice = input('\
1 - Посмотреть контакты\n\
2 - Найти контакт\n\
3 - Добавить контакт\n\
4 - Изменить контакт\n\
5 - Удалить контакт\n\
6 - Просмотреть все контакты\n\
0 - Выйти из приложения\n')
    print()

    if user_choice == '1':
        print(phonebook)
    elif user_choice == '2':
        find_number()
    elif user_choice == '3':
        #add_phone_number(phonebook)
        pass
    elif user_choice == '4':
        #change_phone_number(phonebook)
        pass
    elif user_choice == '5':
        #delete_contact(phonebook)
        pass
    elif user_choice == '6':
        #show_phonebook(phonebook)
        pass
    elif user_choice == '0':
        print('До свидания!')
        break
    else:
        print('Неправильно выбрана команда!')
        print()
        continue
    
    
    
#     import json
# import os

# DATA_JSON = "tel.json"

# def save_js(phonebook) :
#     with open(DATA_JSON, "w", encoding='utf-8') as write_file:
#         json.dump(phonebook, write_file, ensure_ascii=False)

# def load_js() :
#     with open(DATA_JSON, "r", encoding='utf-8') as read_file:
#         ph = json.load(read_file) 
#     return ph 

# def print_key(data):
#     atr = list(data.keys())
#     print(*atr)

# def search(key):
#     pass
    
# phonebook = {
#     "дядя Ваня": { 'phones': [123,321], 
#                   'birthday': '01.01.1960', 
#                   'email': "vanya@mail.ru" } ,
#     "дядя Вася": { 'phones': [22222,33333], 
#                   'birthday': '01.01.2000', 
#                   'email': "vanya@mail.ru" } 
#              }



# if not os.path.exists(DATA_JSON):
#     save_js(phonebook)
# data = load_js()
# # print(data)
# # print(data['дядя Ваня'] ['phones'][-1])  
# print_key(data)
import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_table():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
             (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, phone TEXT)''')
    conn.commit()
    conn.close()

def add_contact():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    phone = entry_phone.get()
    if first_name and last_name and phone:
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute("INSERT INTO contacts (first_name, last_name, phone) VALUES (?, ?, ?)", (first_name, last_name, phone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Выполнено", "Контакт добавлен успешно")
        entry_first_name.delete(0, tk.END)
        entry_last_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        show_contacts()  
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, введите имя, фамилию и номер телефона")

def show_contacts():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    contacts = c.execute("SELECT * FROM contacts").fetchall()
    conn.close()
    if contacts:
        contact_list.delete(0, tk.END)
        for contact in contacts:
            contact_list.insert(tk.END, f"{contact[1]} {contact[2]} {contact[3]}")
    else:
        messagebox.showinfo("Справочник пуст", "Справочник пуст")

def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        contact_info = contact_list.get(index)
        first_name, last_name = contact_info.split(" ")[0], contact_info.split(" ")[1]
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute("DELETE FROM contacts WHERE first_name=? AND last_name=?", (first_name, last_name))
        conn.commit()
        conn.close()
        show_contacts()
    else:
        messagebox.showerror("Ошибка", "Выберите контакт для удаления")

def update_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        contact_info = contact_list.get(index)
        first_name, last_name = contact_info.split(" ")[0], contact_info.split(" ")[1]
        new_phone = entry_phone.get()
        if new_phone:
            conn = sqlite3.connect('phonebook.db')
            c = conn.cursor()
            c.execute("UPDATE contacts SET phone=? WHERE first_name=? AND last_name=?", (new_phone, first_name, last_name))
            conn.commit()
            conn.close()
            messagebox.showinfo("Выполнено", "Контакт успешно обновлен")
            entry_phone.delete(0, tk.END)
            show_contacts()
        else:
            messagebox.showerror("Ошибка", "Введите новый номер телефона")
    else:
        messagebox.showerror("Ошибка", "Выберите контакт для изменения")

create_table()

root = tk.Tk()
root.title("Телефонный справочник")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_first_name = tk.Label(frame_input, text="Имя:")
label_first_name.grid(row=0, column=0, padx=5)
entry_first_name = tk.Entry(frame_input)
entry_first_name.grid(row=0, column=1, padx=5)

label_last_name = tk.Label(frame_input, text="Фамилия:")
label_last_name.grid(row=0, column=2, padx=5)
entry_last_name = tk.Entry(frame_input)
entry_last_name.grid(row=0, column=3, padx=5)

label_phone = tk.Label(frame_input, text="Телефон:")
label_phone.grid(row=0, column=4, padx=5)
entry_phone = tk.Entry(frame_input)
entry_phone.grid(row=0, column=5, padx=5)

button_add = tk.Button(frame_input, text="Добавить контакт", command=add_contact)
button_add.grid(row=0, column=6, padx=5)

frame_list = tk.Frame(root)
frame_list.pack(pady=10)

contact_list = tk.Listbox(frame_list, width=50)
contact_list.pack()

button_show = tk.Button(root, text="Показать все контакты", command=show_contacts)
button_show.pack(pady=10)

button_delete = tk.Button(root, text="Удалить выбранный контакт", command=delete_contact)
button_delete.pack(pady=5)

button_update = tk.Button(root, text="Изменить номер телефона", command=update_contact)
button_update.pack(pady=5)

root.mainloop()

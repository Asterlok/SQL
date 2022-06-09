from tkinter import *
import db

"""Класс окна редактирования БД"""
class Edit_Window:
    def __init__(self, width = 400, height = 600, title='Edit Data'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+300")
        self.root.resizable(False, True)
        self.label = Label(self.root, text = "Edit", font = 18 , bg = '#badbad')

    """Функция добавления артиста"""
    def add_db_artist(self):
        i = self.id_a.get()
        n = self.name.get()
        g = self.genre.get()
        db.add_artist(i,n,g)
        self.id_a.delete(0, END)
        self.name.delete(0, END)
        self.genre.delete(0, END)
        self.label = Label(self.root, text = 'Добавлен!', font = 18 , bg = '#badbad').pack()

    """Функция удаления артиста"""
    def del_db_artist(self):
        n = self.del_name.get()
        db.del_artist(n)
        self.del_name.delete(0, END)
        self.label = Label(self.root, text='Удалён!', font=18, bg='#badbad').pack()

    """Функция добавления импресарио"""
    def add_db_impres(self):
        i = self.id_i.get()
        n = self.name_i.get()
        g = self.genre_i.get()
        db.add_impres(i, n, g)
        self.id_i.delete(0, END)
        self.name_i.delete(0, END)
        self.genre_i.delete(0, END)
        self.label = Label(self.root, text='Добавлен!', font=18, bg='#badbad').pack()

    """Функция удаления импресарио"""
    def del_db_impres(self):
        n_i = self.del_name_i.get()
        db.del_impres(n_i)
        self.del_name_i.delete(0, END)
        self.label = Label(self.root, text='Удалён!', font=18, bg='#badbad').pack()

    """Функция добавления мероприятия"""
    def add_db_active(self):
        i = self.id_ac.get()
        n = self.name_ac.get()
        d = self.date_ac.get()
        b = self.build_ac.get()
        db.add_active(i, n, d, b)
        self.id_ac.delete(0, END)
        self.name_ac.delete(0, END)
        self.date_ac.delete(0, END)
        self.build_ac.delete(0, END)
        self.label = Label(self.root, text='Добавлено!', font=18, bg='#badbad').pack()

    """Функция удаления мероприятия"""
    def del_db_active(self):
        n_a = self.del_name_ac.get()
        db.del_active(n_a)
        self.del_name_ac.delete(0, END)
        self.label = Label(self.root, text='Удалено!', font=18, bg='#badbad').pack()

    """Добавить артиста"""
    def add_artist(self):
       self.id_label = Label(self.root, text='Id').pack()
       self.id_a = Entry(self.root, width=30)
       self.id_a.pack()
       self.name_label = Label(self.root, text='Name').pack()
       self.name = Entry(self.root, width=30)
       self.name.pack()
       self.genre_label = Label(self.root, text='Genre Name').pack()
       self.genre = Entry(self.root, width=30)
       self.genre.pack()
       Button(self.root, width=10, height=4, text="Add", command=self.add_db_artist, bg='#badbad').pack(side=BOTTOM)

    """Удалить артиста"""
    def del_artist(self):
       self.del_name_label = Label(self.root, text='Name').pack()
       self.del_name = Entry(self.root, width=30)
       self.del_name.pack()
       Button(self.root, width=10, height=4, text="Delete", command=self.del_db_artist, bg='#badbad').pack(side=BOTTOM)

    """Добавить импресарио"""
    def add_impres(self):
        self.id_label = Label(self.root, text='Id').pack()
        self.id_i = Entry(self.root, width=30)
        self.id_i.pack()
        self.name_i_label = Label(self.root, text='Name').pack()
        self.name_i = Entry(self.root, width=30)
        self.name_i.pack()
        self.genre_i_label = Label(self.root, text='Genre Id').pack()
        self.genre_i = Entry(self.root, width=30)
        self.genre_i.pack()
        Button(self.root, width=10, height=4, text="Add", command=self.add_db_impres, bg='#badbad').pack(side=BOTTOM)

    """Удалить импресарио"""
    def del_impres(self):
        self.del_name_i_label = Label(self.root, text='Name').pack()
        self.del_name_i = Entry(self.root, width=30)
        self.del_name_i.pack()
        Button(self.root, width=10, height=4, text="Delete", command=self.del_db_impres, bg='#badbad').pack(side=BOTTOM)

    """Добавить мероприятие"""
    def add_active(self):
       self.id_ac_label = Label(self.root, text='Activity Id').pack()
       self.id_ac = Entry(self.root, width=30)
       self.id_ac.pack()
       self.name_ac_label = Label(self.root, text='Name Activity').pack()
       self.name_ac = Entry(self.root, width=30)
       self.name_ac.pack()
       self.date_label = Label(self.root, text='Date Activity').pack()
       self.date_ac = Entry(self.root, width=30)
       self.date_ac.pack()
       self.build_ac_label = Label(self.root, text='Building Id').pack()
       self.build_ac = Entry(self.root, width=30)
       self.build_ac.pack()
       Button(self.root, width=10, height=4, text="Add", command=self.add_db_active, bg='#badbad').pack(side=BOTTOM)

    """Удалить мероприятие"""
    def del_active(self):
        self.del_name_ac_label = Label(self.root, text='Name Activity').pack()
        self.del_name_ac = Entry(self.root, width=30)
        self.del_name_ac.pack()
        Button(self.root, width=10, height=4, text="Delete", command=self.del_db_active, bg='#badbad').pack(side=BOTTOM)

    """Меню"""
    def show_options(self):
        self.my_menu = Menu(self.root)
        self.root.config(menu = self.my_menu)
        self.file_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label = 'Create', menu = self.file_menu)
        self.file_menu.add_command(label="Artists", command = self.add_artist)
        self.file_menu.add_command(label="Impresario", command=self.add_impres)
        self.file_menu.add_command(label="Activity", command=self.add_active)

        self.edit_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='Delete', menu=self.edit_menu)
        self.edit_menu.add_command(label="Artists", command=self.del_artist)
        self.edit_menu.add_command(label="Impresario", command=self.del_impres)
        self.edit_menu.add_command(label="Activity", command=self.del_active)

    def draw_widgets(self):
        self.label.pack()

    def clear(self):
            self.my_label.destroy()

    def run(self):
        self.draw_widgets()
        self.show_options()
        self.root.mainloop()

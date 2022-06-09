from tkinter import *
import db

class Que_Window:
    def __init__(self, width = 900, height = 600, title='Show Queries'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+300")
        self.root.resizable(True, True)
        self.label = Label(self.root, text = "Запрос", font = ("", 16, "") , bg = '#badbad')

    """Очистка окна перед следующим запросом"""
    def clear(self):
        self.res.destroy() #убить вывод
        self.querie.destroy() #убить имя запроса
        self.question.destroy() #убить условие
        self.field.destroy() #убить поле ввода
        self.B.destroy() #убить кнопку
        self.field_1.destroy() #убить поле ввода 2, если есть
        self.question_1.destroy() #убить условие_2, если есть

    """Запрос в БД и вывод оттуда"""
    def que_1_db(self):
        capacity = self.field.get()
        self.q1 = db.que_1(capacity)
        self.res = Label(self.root, text = self.q1)
        self.res.pack()

    """Окно запроса и ввода параметра"""
    def show_1(self):
        self.querie = Label(self.root, text="1. Получить перечень культурных сооружений указанного типа,"
                                           "удовлетворяющих заданным характеристикам. ", font = 14 , bg = '#badbad')
        self.querie.pack()
        self.question = Label(self.root, text='Вместительность не менее:')
        self.question.pack()
        self.field = Entry(self.root, width=30)
        self.field.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_1_db,
               bg='#badbad')
        self.B.pack(side=BOTTOM)

    def que_2_db(self):
        genre = self.field.get()
        self.q2 = db.que_2(genre)
        self.res = Label(self.root, text = self.q2)
        self.res.pack()

    def show_2(self):
        self.querie = Label(self.root, text="2.	Получить список артистов, выступающих в некотором жанре.", font = 14 , bg = '#badbad')
        self.querie.pack()
        self.question = Label(self.root, text='Жанр:')
        self.question.pack()
        self.field = Entry(self.root, width=30)
        self.field.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_2_db,
               bg='#badbad')
        self.B.pack(side=BOTTOM)

    def que_3_db(self):
        name = self.field.get()
        self.q3= db.que_3(name)
        self.res = Label(self.root, text = self.q3)
        self.res.pack()

    def show_3(self):
        self.querie = Label(self.root, text="3.	Получить список артистов, работающих с некоторым импресарио.", font = 14 , bg = '#badbad')
        self.querie.pack()
        self.question = Label(self.root, text='Импресарио:')
        self.question.pack()
        self.field = Entry(self.root, width=30)
        self.field.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_3_db,
               bg='#badbad')
        self.B.pack(side=BOTTOM)

    def que_4_db(self):
        self.q4= db.que_4()
        self.res = Label(self.root, text = self.q4)
        self.res.pack()

    def show_4(self):
        self.querie = Label(self.root, text="4.	Получить список артистов, работающих более чем"
                                            " c одним импресарио.", font = 14 , bg = '#badbad')
        self.querie.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_4_db,
               bg='#badbad')
        self.B.pack(side=BOTTOM)

    def que_5_db(self):
        name = self.field.get()
        self.q5 = db.que_5(name)
        self.res = Label(self.root, text=self.q5)
        self.res.pack()

    def show_5(self):
        self.querie = Label(self.root, text="5.	Получить список импресарио указанного артиста.", font = 14 , bg = '#badbad')
        self.querie.pack()
        self.question = Label(self.root, text='Имя артиста:')
        self.question.pack()
        self.field = Entry(self.root, width=30)
        self.field.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_5_db,
               bg='#badbad')
        self.B.pack(side=BOTTOM)

    def que_6_db(self):
        date_1 = self.field.get()
        date_2 = self.field_1.get()
        self.q6 = db.que_6(date_1, date_2)
        self.res = Label(self.root, text=self.q6)
        self.res.pack()

    def show_6(self):
        self.querie = Label(self.root, text="6.	Получить перечень концертных мероприятий,"
                                            " проведенных в течение заданного периода времени.", font=14,
                            bg='#badbad')
        self.querie.pack()
        self.question = Label(self.root, text='С числа [ГГГГ-ММ-ДД]:')
        self.question.pack()
        self.field = Entry(self.root, width=30)
        self.field.pack()
        self.question_1 = Label(self.root, text='по число [ГГГГ-ММ-ДД]:')
        self.question_1.pack()
        self.field_1 = Entry(self.root, width=30)
        self.field_1.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_6_db,
                        bg='#badbad')
        self.B.pack(side=BOTTOM)

    def que_7_db(self):
        name = self.field.get()
        self.q7 = db.que_7(name)
        self.res = Label(self.root, text=self.q7)
        self.res.pack()

    def show_7(self):
        self.querie = Label(self.root, text="7.	Получить список призеров указанного конкурса. ", font=14,
                            bg='#badbad')
        self.querie.pack()
        self.question = Label(self.root, text='Конкурс:')
        self.question.pack()
        self.field = Entry(self.root, width=30)
        self.field.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_7_db,
                        bg='#badbad')
        self.B.pack(side=BOTTOM)

    def que_8_db(self):
        name = self.field.get()
        self.q8 = db.que_8(name)
        self.res = Label(self.root, text=self.q8)
        self.res.pack()

    def show_8(self):
        self.querie = Label(self.root, text="8.	Получить перечень мероприятий,"
                                            "проведенных в указанном культурном сооружении ", font=14, bg='#badbad')
        self.querie.pack()
        self.question = Label(self.root, text='Название сооружения:')
        self.question.pack()
        self.field = Entry(self.root, width=30)
        self.field.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_8_db,
                        bg='#badbad')
        self.B.pack(side=BOTTOM)

    def que_9_db(self):
        name = self.field.get()
        self.q9 = db.que_9(name)
        self.res = Label(self.root, text=self.q9)
        self.res.pack()

    def show_9(self):
        self.querie = Label(self.root, text="9. Получить список импресарио определенного жанра.", font=14, bg='#badbad')
        self.querie.pack()
        self.question = Label(self.root, text='Название жанра:')
        self.question.pack()
        self.field = Entry(self.root, width=30)
        self.field.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_9_db,
                        bg='#badbad')
        self.B.pack(side=BOTTOM)

    def que_10_db(self):
        date = self.field.get()
        self.q10 = db.que_10(date)
        self.res = Label(self.root, text=self.q10)
        self.res.pack()

    def show_10(self):
        self.querie = Label(self.root, text="10. Получить список артистов, участвовавших в конкурсах "
                                            "до определенного периода времени.", font=14, bg='#badbad')
        self.querie.pack()
        self.question = Label(self.root, text='До периода [ГГГГ-ММ-ДД]:')
        self.question.pack()
        self.field = Entry(self.root, width=30)
        self.field.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_10_db,
                        bg='#badbad')
        self.B.pack(side=BOTTOM)

    def que_11_db(self):
        date = self.field.get()
        self.q11 = db.que_11(date)
        self.res = Label(self.root, text=self.q11)
        self.res.pack()

    def show_11(self):
        self.querie = Label(self.root, text="11. Получить список организаторов мероприятий "
                                            "и число проведенных ими концертов\nв течение"
                                            " определенного периода времени. ", font=14, bg='#badbad')
        self.querie.pack()
        self.question = Label(self.root, text='От периода [ГГГГ-ММ-ДД]:')
        self.question.pack()
        self.field = Entry(self.root, width=30)
        self.field.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_11_db,
                        bg='#badbad')
        self.B.pack(side=BOTTOM)

    def que_12_db(self):
        date_1 = self.field.get()
        date_2 = self.field_1.get()
        self.q12 = db.que_12(date_1, date_2)
        self.res = Label(self.root, text=self.q12)
        self.res.pack()

    def show_12(self):
        self.querie = Label(self.root, text="12. Получить перечень культурных сооружений,"
                                            "\nа также даты проведения на них культурных мероприятий"
                                            " в течение определенного периода времени. ", font=14, bg='#badbad')
        self.querie.pack()
        self.question = Label(self.root, text='От периода [ГГГГ-ММ-ДД]:')
        self.question.pack()
        self.field = Entry(self.root, width=30)
        self.field.pack()
        self.question_1 = Label(self.root, text='до периода [ГГГГ-ММ-ДД]:')
        self.question_1.pack()
        self.field_1 = Entry(self.root, width=30)
        self.field_1.pack()
        self.B = Button(self.root, width=10, height=4, text="Отправить", command=self.que_12_db,
                        bg='#badbad')
        self.B.pack(side=BOTTOM)

    """Меню"""
    def show_options(self):
        self.my_menu = Menu(self.root)
        self.root.config(menu = self.my_menu)
        self.file_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label = 'Queries', menu = self.file_menu)
        self.file_menu.add_command(label="1", command = self.show_1)
        self.file_menu.add_command(label="2", command=self.show_2)
        self.file_menu.add_command(label="3", command=self.show_3)
        self.file_menu.add_command(label="4", command=self.show_4)
        self.file_menu.add_command(label="5", command=self.show_5)
        self.file_menu.add_command(label="6", command=self.show_6)
        self.file_menu.add_command(label="7", command=self.show_7)
        self.file_menu.add_command(label="8", command=self.show_8)
        self.file_menu.add_command(label="9", command=self.show_9)
        self.file_menu.add_command(label="10", command=self.show_10)
        self.file_menu.add_command(label="11", command=self.show_11)
        self.file_menu.add_command(label="12", command=self.show_12)

    def draw_widgets(self):
        self.label.pack()

    """Очистка окна перед следующим запросом"""
    def clear(self):
        self.res.destroy() #убить вывод
        self.querie.destroy() #убить имя запроса
        self.question.destroy() #убить условие
        self.field.destroy() #убить поле ввода
        self.B.destroy() #убить кнопку
        self.field_1.destroy() #убить поле ввода 2, если есть
        self.question_1.destroy() #убить условие_2, если есть

    def draw_button(self):
        Button(self.root,width=10, height=4, text="Clear", command = self.clear, bg='#badbad').pack(side = BOTTOM)

    def run(self):
        self.draw_widgets()
        self.draw_button()
        self.show_options()
        self.root.mainloop()

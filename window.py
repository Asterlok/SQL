from tkinter import *
from show_data import Show_Window
from edit_data import Edit_Window
from show_que import Que_Window

class Window:
    def __init__(self, width = 300, height = 250, title='Philharmonic'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+300")
        self.root.resizable(False, False)
        self.label = Label(self.root, text = "Philharmonic Database", font = 18 , bg = '#badbad')

    def draw_widgets(self):
        self.label.pack()

    """Окно входа в демонстрацию базы данных"""
    def show(self):
        s = Show_Window()
        s.run()

    """Окно входа в редактирование базы данных"""
    def edit(self):
        e = Edit_Window()
        e.run()

    """Окно входа в просмотр запросов к бд"""
    def queries(self):
        q = Que_Window()
        q.run()

    def draw_buttons(self):
        Button(self.root, width=10, height=4, text="Show Data", command = self.show).pack()
        Button(self.root, width=10, height=4, text="Edit Data", command = self.edit).pack()
        Button(self.root, width=10, height=4, text="Show Queries", command = self.queries).pack()

    def run(self):
        self.draw_widgets()
        self.draw_buttons()
        self.root.mainloop()


from tkinter import *
import db

class Show_Window:
    def __init__(self, width = 400, height = 600, title='Show Data'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+300")
        self.root.resizable(False, True)
        self.label = Label(self.root, text = "Data", font = 18 , bg = '#badbad')


    def clear(self):
        self.label.destroy()

    """Список артистов"""
    def show_artist(self):
        self.data = db.show_artist()
        Label(self.root, text = "Artists: ", font = 18 , bg = '#badbad').pack()
        self.my_label = Label(self.root, text = self.data)
        self.my_label.pack()

    """Список импресарио"""
    def show_impresario(self):
        self.data = db.show_impresario()
        Label(self.root, text="Impresario: ", font=18, bg='#badbad').pack()
        self.my_label = Label(self.root, text = self.data)
        self.my_label.pack()

    """Список сооружений"""
    def show_building(self):
        self.data = db.show_building()
        Label(self.root, text="Building: ", font=18, bg='#badbad').pack()
        self.my_label = Label(self.root, text=self.data)
        self.my_label.pack()

    """Список мероприятий"""
    def show_activity(self):
        self.data = db.show_activity()
        Label(self.root, text="Activity: ", font=18, bg='#badbad').pack()
        self.my_label = Label(self.root, text=self.data)
        self.my_label.pack()

    """Меню"""
    def show_options(self):
        self.my_menu = Menu(self.root)
        self.root.config(menu = self.my_menu)
        self.file_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label = 'Show', menu = self.file_menu)
        self.file_menu.add_command(label="Artists", command = self.show_artist)
        self.file_menu.add_command(label="Impresario", command=self.show_impresario)
        self.file_menu.add_command(label="Buildings", command=self.show_building)
        self.file_menu.add_command(label="Activity", command=self.show_activity)

    def draw_widgets(self):
        self.label.pack()

    def clear(self):
            self.my_label.destroy()

    def draw_button(self):
        Button(self.root,width=10, height=4, text="Clear", command = self.clear, bg='#badbad').pack(side = BOTTOM)

    def run(self):
        self.draw_widgets()
        self.draw_button()
        self.show_options()
        self.root.mainloop()

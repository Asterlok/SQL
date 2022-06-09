import db
from tkinter import *

class DefaultButton(tk.Frame):
    """Дефолтный конструктор кнопок"""
    def __init__(self, toolbar, text, command, side='l'):
        super().__init__(toolbar)
        btn_open_dialog = tk.Button(toolbar, text=text, command=command, bg='#e3f2fd', bd=0,
                                    compound=tk.TOP)
        if side == 'r':
            btn_open_dialog.pack(side=tk.RIGHT)
        elif side == 'c':
            btn_open_dialog.pack(side=tk.LEFT, expand = tk.YES)
        else:
            btn_open_dialog.pack(side=tk.LEFT)
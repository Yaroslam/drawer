import tkinter as tk
import Imager


class Opener(tk.Toplevel):  # конструктор класса
    def __init__(self):
        super().__init__()
        self.init_opener()
        self.render_ui()
        self.img = Imager.Image

    def init_opener(self):
        self.title('открыть файл')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        self.window = tk.Frame(self, height=220, width=400, bg='green')

        self.back_btn = tk.Button(self, bg='black')

        self.ok_btn = tk.Button(self, bg='black')

    def render_ui(self):
        self.window.pack()
        self.back_btn.place(x=350, y=210)
        self.ok_btn.place(x=380, y=210)

    def pick_file(self, name):
        pass

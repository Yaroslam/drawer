import tkinter as tk
from const import *
import Imager
import File_work


# TODO LIST
# цветовая палитра 1/2
# работа с файлами 40/100
# создать кнопку file, по нажатию на которую будет открывать окно для работы с файлами, отккрыть или созранить файл
# при нажатии на них будет открываться еще одно диалоговое окно, для каждого из них
# оформить все по человечески 10/100


class Main(tk.Frame):  # конструктор класса
    def __init__(self, root):
        super().__init__(root)
        self.img = Imager.Imager()
        self.FW = File_work.File_work()
        self.__init_main__()
        self.render_ui()

    def __init_main__(self):  # главная функции
        self.FW.is_dir_real()

        self.current_color = CURRENT_COLOR
        self.coordinate = COORDINATE

        self.toolbar = tk.Frame(bg=COLORS[1], height=300, width=125)

        self.work_place = tk.Canvas(bg="white", height=300, width=500)

        self.up_button = tk.Button(bg="red")  # конпки управления
        self.up_button.bind('<Button-1>', lambda event: self.calculate_pos(0, -1))

        self.right_button = tk.Button(bg="red")
        self.right_button.bind('<Button-1>', lambda event: self.calculate_pos(1, 0))

        self.down_button = tk.Button(bg="red")
        self.down_button.bind('<Button-1>', lambda event: self.calculate_pos(0, 1))

        self.left_button = tk.Button(bg="red")
        self.left_button.bind('<Button-1>', lambda event: self.calculate_pos(-1, 0))

        self.draw_button = tk.Button(bg="blue")
        self.draw_button.bind('<Button-1>', lambda event: self.draw_pixel())

        self.next_color = tk.Button(bg='green')  # кнопки смены цвета
        self.next_color.bind('<Button-1>', lambda event: self.change_color(1))

        self.previous_color = tk.Button(bg='green')
        self.previous_color.bind('<Button-1>', lambda event: self.change_color(-1))

        self.save_button = tk.Button(bg='purple', text='save')
        self.save_button.bind('<Button-1>', lambda event: self.get_img())

        self.open_button = tk.Button(bg='purple', text='open')
        self.open_button.bind('<Button-1>', lambda event: self.create_img())

        self.point = self.render_point(COLORS[self.current_color])  # каретка

    def check_pos(self, change_x, change_y):  # проверка нахождния координат в пределах work_place
        if self.coordinate[0] + change_x - 2 < 0 or self.coordinate[0] + change_x + 2 > 500:
            return False
        if self.coordinate[1] + change_y - 2 < 0 or self.coordinate[1] + change_y + 3 > 300:
            return False
        return True

    def render_point(self, color):  # рисуем каретку
        return self.work_place.create_rectangle(self.coordinate[0], self.coordinate[1], self.coordinate[0] + 3,
                                                self.coordinate[1] + 3, fill=color, outline=color)

    def calculate_pos(self, change_x, change_y):  # смена координат для коретки
        self.work_place.delete(self.point)
        if not self.check_pos(change_x, change_y):
            self.point = self.render_point(COLORS[self.current_color])
            return self.coordinate
        else:
            self.coordinate[0] += change_x
            self.coordinate[1] += change_y
            self.point = self.render_point(COLORS[self.current_color])
            return self.coordinate

    def change_color(self, next_or_prev):  # выбираем цывет
        self.work_place.delete(self.point)
        self.current_color += next_or_prev
        self.point = self.render_point(COLORS[self.current_color])
        print(self.current_color)

    def draw_pixel(self):  # ставим пиксель
        self.work_place.create_rectangle(self.coordinate[0], self.coordinate[1], self.coordinate[0] + 3,
                                         self.coordinate[1] + 3, fill=COLORS[self.current_color],
                                         outline=COLORS[self.current_color])
        print(self.coordinate)

    def get_img(self):  # сохраняем картинку
        x = root.winfo_rootx()
        y = root.winfo_rooty()
        x1 = x + self.work_place.winfo_width()
        y1 = y + self.work_place.winfo_height()
        self.work_place.delete(self.point)
        self.FW.save_file(x, y, x1, y1)

    def create_img(self):  # вставляем картинку
        self.work_place.image = self.FW.open_file()
        self.work_place.create_image(0, 0, anchor='nw', image=self.work_place.image)
        self.point = self.render_point(COLORS[self.current_color])

    def render_ui(self):  # рендер всех элементов
        self.work_place.place(x=10, y=30)
        self.toolbar.place(x=517, y=32)
        self.up_button.place(x=570, y=100)
        self.right_button.place(x=585, y=130)
        self.down_button.place(x=570, y=160)
        self.left_button.place(x=555, y=130)
        self.draw_button.place(x=570, y=130)
        self.next_color.place(x=585, y=190)
        self.previous_color.place(x=555, y=190)
        self.save_button.place(x=10, y=0)
        self.open_button.place(x=50, y=0)


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("draw")
    root.geometry("650x340+300+200")
    root.resizable(False, False)
    root.mainloop()

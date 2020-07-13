import tkinter as tk
from const import COLORS

#TODO LIST
#цветовая палитра 1/2
#работа с файлами 0/100
#вынести нахуй current color и массив позиций в конст 0/1
#обработать out of range для массива цветов 0/1




class Main(tk.Frame): #конструктор класса
    def __init__(self, root):

        super().__init__(root)
        self.current_color = 0
        self.coordinate = [10, 10]
        self.__init_main()
        self.render_ui()
        self.point = self.render_point(COLORS[self.current_color])


    def __init_main(self):  # главная функции
        self.toolbar = tk.Frame(bg="black", height=295, width=125)

        self.work_place = tk.Canvas(bg="white", height=300, width=500)

        self.up_button = tk.Button(bg="red")
        self.right_button = tk.Button(bg="red")
        self.down_button = tk.Button(bg="red")
        self.left_button = tk.Button(bg="red")
        self.draw_button = tk.Button(bg="blue")

        self.next_color = tk.Button(bg='green')
        self.previous_color = tk.Button(bg='green')

        self.up_button.bind('<Button-1>', lambda event: self.calculate_pos(0,-1))
        self.right_button.bind('<Button-1>', lambda event: self.calculate_pos(1, 0))
        self.down_button.bind('<Button-1>', lambda event: self.calculate_pos(0, 1))
        self.left_button.bind('<Button-1>', lambda event: self.calculate_pos(-1, 0))
        self.draw_button.bind('<Button-1>', lambda event: self.draw_pixel())

        self.next_color.bind('<Button-1>', lambda event: self.change_color(1))
        self.previous_color.bind('<Button-1>', lambda event: self.change_color(-1))

    def check_pos(self, change_x, change_y): #проверка нахождния координат в пределах work_place
        if self.coordinate[0] + change_x-2 < 0 or self.coordinate[0] + change_x+2 > 500:
            return False
        if self.coordinate[1] + change_y-2 < 0 or self.coordinate[1] + change_y+3 > 300:
            return False
        return True


    def render_point(self, color): #рисуем каретку
       return self.work_place.create_rectangle(self.coordinate[0], self.coordinate[1], self.coordinate[0]+3,
                                         self.coordinate[1]+3, fill=color, outline=color)


    def calculate_pos(self, change_x, change_y): #смена координат для коретки
        self.work_place.delete(self.point)
        if self.check_pos(change_x, change_y) == False:
            self.point = self.render_point()
            return self.coordinate
        else:
            self.coordinate[0] += change_x
            self.coordinate[1] += change_y
            self.point = self.render_point(COLORS[self.current_color])
            return self.coordinate


    def change_color(self, next_or_prev): #выбираем цывет
        self.work_place.delete(self.point)
        self.current_color+=next_or_prev
        self.point = self.render_point(COLORS[self.current_color])
        print(self.current_color)

    def draw_pixel(self): #ставим пиксель
        self.work_place.create_rectangle(self.coordinate[0], self.coordinate[1], self.coordinate[0]+3,
                                         self.coordinate[1]+3, fill=COLORS[self.current_color],
                                         outline=COLORS[self.current_color])
        print(self.coordinate)


    def render_ui(self): #рендер всех элементов
        self.work_place.place(x=10, y=10)
        self.toolbar.place(x=520, y=10)
        self.up_button.place(x=570, y=100)
        self.right_button.place(x=585, y=130)
        self.down_button.place(x=570, y =160)
        self.left_button.place(x=555, y =130)
        self.draw_button.place(x=570,y=130)
        self.next_color.place(x=585, y=190)
        self.previous_color.place(x=555 ,y=190)


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("draw")
    root.geometry("650x340+300+200")
    root.resizable(True, True)
    root.mainloop()

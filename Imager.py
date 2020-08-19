import PIL as pl
import os
from const import DIR_NAME
from PIL import Image
from PIL import ImageTk
from PIL import ImageGrab


class Imager:

    def save_IMG(self, file_name, x, y, x1, y1):
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_name)

    def open_IMG(self, file_name):  # НАХУЙ НЕ РАБОТАЕТ
        pilImage = Image.open(file_name)
        image = ImageTk.PhotoImage(pilImage)
        return image


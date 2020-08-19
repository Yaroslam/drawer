from tkinter import filedialog as fd
import Imager
from const import *


class File_work():
    def __init__(self):
        self.IMG = Imager.Imager()

    def open_file(self):
        file_name = fd.askopenfilename(defaultextension='.jpg',
                  filetypes=[('PNG pictures','*.png'),
                             ('JPEG pictures','*.jpg')],
                                       initialdir=PATH+DIR_NAME)
        return self.IMG.open_IMG(file_name=file_name)

    def save_file(self, x, y, x1, y1):
        file_name = fd.asksaveasfilename(defaultextension='.jpg',
                  filetypes=[('PNG pictures','*.png'),
                             ('JPEG pictures','*.jpg')],
                                       initialdir=PATH+DIR_NAME)
        self.IMG.save_IMG(file_name, x, y, x1, y1)

    def is_dir_real(self):
        if not os.path.exists(DIR_NAME):
            os.mkdir(DIR_NAME, mode=0o777)
        else:
            pass


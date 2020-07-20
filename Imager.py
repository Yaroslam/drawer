import PIL as pl
import os


class Image:
    def save_IMG(self, widget, root):
        x = root.winfo_rootx() + widget.winfo_x()
        y = root.winfo_rooty() + widget.winfo_y()
        x1 = x + widget.winfo_width()
        y1 = y + widget.winfo_height()
        pl.ImageGrab.grab().crop((x, y, x1, y1)).save()

    def open_IMG(self, file_name):
        pilImage = pl.Image.open(file_name)
        image = pl.ImageTk.PhotoImage(pilImage)
        return image

    def is_dir_real(self, dir_name):
        if not os.path.exists(dir_name):
            os.mkdir(dir_name, mode=0o777)
        else:
            pass

    def get_files(self, path):
        return os.listdir(path)

import os
import pathlib
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

#C:\Users\Samur\Desktop\Тестовая папка_2\Тестовый_файл.txt


class FileManager:


    @staticmethod
    def get_rgb(rgb):
        return "#%02x%02x%02x" % rgb

    def create_new_file_in_directory(self):
        new_file_path = self.first_directory_enter_label.get()
        try: open(new_file_path, "w"), showinfo(title="Информация", message="Файл успешно добавлен в директорию"), self.first_directory_enter_label.delete(0, END)
        except FileNotFoundError: showerror(title="Ошибка", message="Неправильное указание директории"), self.first_directory_enter_label.delete(0, END)


    def delete_file_from_directory(self):
        delete_file_path = self.second_directory_enter_label.get()
        try: os.remove(delete_file_path), showinfo(title="Информация", message="Файл успешно удален из директории"), self.second_directory_enter_label.delete(0, END)
        except FileNotFoundError: showerror(title="Ошибка", message="Неправильное указание директории"), self.second_directory_enter_label.delete(0, END)

    def replace_file_directory(self):
        old_file_directory = self.third_directory_enter_label.get()
        new_file_directory = self.third_directory_enter_label_2.get()
        try: os.replace(old_file_directory, new_file_directory), showinfo(title="Информация", message="Директория файла успешно заменена"), self.third_directory_enter_label.delete(0, END), self.third_directory_enter_label_2.delete(0, END)
        except FileNotFoundError: showerror(title="Ошибка", message="Неправильное указание директории"), self.third_directory_enter_label.delete(0, END), self.third_directory_enter_label_2.delete(0, END)



    def __init__(self):
        self.command_label = Label(text="Выберите операцию с файлом", font="8", background=self.get_rgb((211, 211, 211)))
        self.button_create_new_file = Button(text="Добавить файл в директорию", command=self.create_new_file_in_directory)
        self.button_delete_file = Button(text=" Удалить файл из директории ", command=self.delete_file_from_directory)
        self.button_replace_file_directory = Button(text="         Переместить файл           ", command=self.replace_file_directory)
        self.first_directory_enter_label = Entry()
        self.second_directory_enter_label = Entry()
        self.third_directory_enter_label = Entry()
        self.third_directory_enter_label_2 = Entry()



    def place_vidgets(self):
        self.command_label.place(x=5, y=15)
        self.button_create_new_file.place(x=5, y=50)
        self.button_delete_file.place(x=5, y=80)
        self.button_replace_file_directory.place(x=5, y=110)
        self.first_directory_enter_label.place(x=185, y=53)
        self.second_directory_enter_label.place(x=185, y=83)
        self.third_directory_enter_label.place(x=185, y=113)
        self.third_directory_enter_label_2.place(x=315, y=113)





window = Tk()
window.title("Файловый менеджер"), window.geometry("450x400"), window.resizable(False, False)
ttk.Style().configure(".", font="helvetica 13")
file_manager = FileManager()
file_manager.place_vidgets()
window.mainloop()
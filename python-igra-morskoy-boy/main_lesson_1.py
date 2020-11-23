# импорт модулей
from tkinter import *
from tkinter import messagebox

import time

# создадим рабочую область
tk = Tk()

# создадим переменную для сообщения что наше приложение все еще работает, будет иметь "булевское" значение
app_runing = True

# окно приложения сделаем фиксированными, это будкм определять через переменные
size_canvas_x = 600
size_canvas_y = 600

# close window

# функция закрытия окна
def on_closing():
    global app_runing
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры ???"):
        app_runing = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)

# определяем параметры нашего окна
tk.title("Игра Морской бой")
# запрет изменения размера окна
tk.resizable(0, 0)
# параметр, что наше окно находиться поверх всех окон
tk.wm_attributes("-topmost", 1)
# работа с окном
canvas = Canvas(tk, width=size_canvas_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.pack()
tk.update()


# цикл для работы приложения
while app_runing:
    if app_runing:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
    
    
    
    

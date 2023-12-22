import tkinter as tk
from tkinter import ttk

def submit_button_clicked():
    # Действия при нажатии кнопки "Submit" на второй вкладке
    print("Submit button clicked on Tab 2")
    # Получение значения из поля ввода на второй вкладке
    input_value = input_entry.get()
    print("Input value on Tab 2:", input_value)

def create_tab2(tab_control):
    # Создание второй вкладки
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Вкладка 2')

    # Создание поля ввода и его описания на второй вкладке
    input_label = ttk.Label(tab2, text="Введите текст на второй вкладке:")
    input_label.grid(row=0, column=0, padx=5, pady=5)
    input_entry = ttk.Entry(tab2)
    input_entry.grid(row=0, column=1, padx=5, pady=5)

    # Создание кнопки "Submit" на второй вкладке
    submit_button = ttk.Button(tab2, text="Submit", command=submit_button_clicked)
    submit_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
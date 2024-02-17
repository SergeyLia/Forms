import tkinter as tk
from tkinter import ttk


def create_tab2(tab_control):
    # Создание второй вкладки
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Лист 1')

    # Создание поля ввода и его описания на второй вкладке
    #Создание заголовка на два столбца
    title_label0 = ttk.Label(tab2, text="Жилое помещение предоставлено", font=("Arial", 10, "bold"))
    title_label0.grid(row=0, column=0, columnspan=4, padx=2, pady=1)

    # Создание горизонтальной черты на первой вкладке
    separator = ttk.Separator(tab2, orient='horizontal')
    separator.grid(row=1, column=0, columnspan=4, sticky='ew', padx=2, pady=1)

    input_label = ttk.Label(tab2, text="ФИО:")
    input_label.grid(row=2, column=0, padx=2, sticky='w', pady=2)
    input_entry1 = tk.Text(tab2, height=1, width=20)
    input_entry1.grid(row=3, column=0, columnspan=4, sticky='ew', padx=2, pady=2)

    input_label = ttk.Label(tab2, text="Дата рождения:")
    input_label.grid(row=4, column=0, padx=2, sticky='e', pady=2)
    input_entry2 = tk.Text(tab2, height=1, width=20)
    input_entry2.grid(row=4, column=1, padx=2, pady=2)

    input_label = ttk.Label(tab2, text="Свидетельство о гос. регистрации:")
    input_label.grid(row=5, column=0, columnspan=2, padx=2, sticky='w', pady=2)
    input_entry3 = tk.Text(tab2, height=1, width=20)
    input_entry3.grid(row=6, column=0, columnspan=4, sticky='ew', padx=2, pady=2)

    citizenship_label = ttk.Label(tab2, text="Документ:")
    citizenship_label.grid(row=7, column=0, sticky='e', padx=2, pady=2)
    citizenship_combobox0 = ttk.Combobox(tab2, values=["Свидетельство", "Не свидетельство"])
    citizenship_combobox0.grid(row=7, column=1, sticky='ew', padx=2, pady=2)

    input_label = ttk.Label(tab2, text="серия:")
    input_label.grid(row=8, column=0, padx=2, sticky='e', pady=2)
    input_entry4 = tk.Text(tab2, height=1, width=20)
    input_entry4.grid(row=8, column=1, padx=2, pady=2)

    input_label = ttk.Label(tab2, text="номер:")
    input_label.grid(row=8, column=2, padx=2, sticky='ew', pady=2)
    input_entry5 = tk.Text(tab2, height=1, width=20)
    input_entry5.grid(row=8, column=3, sticky='ew', padx=2, pady=2)

    input_label = ttk.Label(tab2, text="Дата выдачи:")
    input_label.grid(row=9, column=0, padx=2, sticky='e', pady=2)
    input_entry6 = tk.Text(tab2, height=1, width=20)
    input_entry6.grid(row=9, column=1, padx=2, pady=2)

    input_label = ttk.Label(tab2, text="Действителен до:")
    input_label.grid(row=9, column=2, padx=2, sticky='ew', pady=2)
    input_entry7 = tk.Text(tab2, height=1, width=20)
    input_entry7.grid(row=9, column=3, sticky='ew', padx=2, pady=2)

    input_label = ttk.Label(tab2, text="Кем выдан:")
    input_label.grid(row=10, column=0, columnspan=1, padx=2, sticky='w', pady=2)
    input_entry8 = tk.Text(tab2, height=3, width=20)
    input_entry8.grid(row=11, column=0, columnspan=4, sticky='ew', padx=2, pady=2)

    input_label = ttk.Label(tab2, text="Код подразделения:")
    input_label.grid(row=12, column=0, padx=2, sticky='ew', pady=2)
    input_entry9 = tk.Text(tab2, height=1, width=20)
    input_entry9.grid(row=12, column=1, sticky='ew', padx=2, pady=2)

    input_label = ttk.Label(tab2, text="Родство с заявителем:")
    input_label.grid(row=13, column=0, columnspan=2, padx=2, sticky='w', pady=2)
    input_entry10 = tk.Text(tab2, height=1, width=20)
    input_entry10.grid(row=14, column=0, columnspan=4, sticky='ew', padx=2, pady=2)

    check_var = tk.IntVar()
    check_button = ttk.Checkbutton(tab2, text="Владелец проживает по другому адресу", variable=check_var)
    check_button.grid(row=15, column=0, columnspan=3, sticky='ew', padx=2, pady=2)

    input_label = ttk.Label(tab2, text="Основания для вселения (снятия с регистрации):")
    input_label.grid(row=16, column=0, columnspan=2, padx=2, sticky='w', pady=2)
    input_entry11 = tk.Text(tab2, height=1, width=20)
    input_entry11.grid(row=17, column=0, columnspan=4, sticky='ew', padx=2, pady=2)

    input_label = ttk.Label(tab2, text="Свидетельство о регистрации:")
    input_label.grid(row=18, column=0, columnspan=2, padx=2, sticky='w', pady=2)
    input_entry12 = tk.Text(tab2, height=1, width=20)
    input_entry12.grid(row=19, column=0, columnspan=4, sticky='ew', padx=2, pady=2)

    check_var = tk.IntVar()
    check_button1 = ttk.Checkbutton(tab2, text="Несовершеннолетний", variable=check_var)
    check_button1.grid(row=0, column=4, columnspan=3, sticky='ew', padx=2, pady=2)

    check_var = tk.IntVar()
    check_button2 = ttk.Checkbutton(tab2, text="Помещение законного представителя", variable=check_var)
    check_button2.grid(row=1, column=4, columnspan=3, sticky='ew', padx=2, pady=2)
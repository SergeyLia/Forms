import tkinter as tk
from tkinter import ttk
from tab2 import create_tab2

def submit_button_clicked():
    # Действия при нажатии кнопки "Submit" на первой вкладке
    print("Submit button clicked on Tab 1")
    # Получение значения из поля ввода на первой вкладке
    input_value = input_entry.get()
    print("Input value on Tab 1:", input_value)

# Создание главного окна
root = tk.Tk()
root.title("Forms")

# Создание вкладок
tab_control = ttk.Notebook(root)

# Создание первой вкладки
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Основные данные')

# Вызов функции для создания второй вкладки
create_tab2(tab_control)

# Добавление вкладок на главное окно
tab_control.pack(expand=1, fill='both')

# Создание поля ввода и его описания на первой вкладке

citizenship_label = ttk.Label(tab1, text="ОВМ:")
citizenship_label.grid(row=0, column=0, padx=5, pady=2)
citizenship_combobox1 = ttk.Combobox(tab1, values=["Ленинсткий", "Заводской", "Кировский", "Фрунзенский", "Октябрьский"])
citizenship_combobox1.grid(row=0, column=1, padx=5, pady=2)

citizenship_label = ttk.Label(tab1, text="Гражданство:")
citizenship_label.grid(row=1, column=0, padx=5, pady=2)
citizenship_combobox2 = ttk.Combobox(tab1, values=["РОССИЯ", "КАЗАХСТАН", "УЗБЕКИСТАН"])
citizenship_combobox2.grid(row=1, column=1, padx=5, pady=2)

# Создание заголовка на два столбца
title_label = ttk.Label(tab1, text="Персональные данные", font=("Arial", 10, "bold"))
title_label.grid(row=2, column=0, columnspan=2, padx=5, pady=1)

# Создание горизонтальной черты на первой вкладке
separator = ttk.Separator(tab1, orient='horizontal')
separator.grid(row=3, columnspan=2, sticky='ew', padx=5, pady=1)

citizenship_label = ttk.Label(tab1, text="Пол:")
citizenship_label.grid(row=4, column=0, padx=5, pady=2)
citizenship_combobox3 = ttk.Combobox(tab1, values=["МУЖ", "ЖЕН"])
citizenship_combobox3.grid(row=4, column=1, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Фамилия:")
input_label.grid(row=5, column=0, padx=5, pady=2)
input_entry1 = ttk.Entry(tab1)
input_entry1.grid(row=5, column=1, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Фамилия род.:")
input_label.grid(row=6, column=0, padx=5, pady=2)
input_entry2 = ttk.Entry(tab1)
input_entry2.grid(row=6, column=1, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Имя:")
input_label.grid(row=7, column=0, padx=5, pady=2)
input_entry3 = ttk.Entry(tab1)
input_entry3.grid(row=7, column=1, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Отчество:")
input_label.grid(row=7, column=0, padx=5, pady=2)
input_entry4 = ttk.Entry(tab1)
input_entry4.grid(row=7, column=1, padx=5, pady=2)

# Создание заголовка на два столбца
title_label = ttk.Label(tab1, text="Сведения о рождении", font=("Arial", 10, "bold"))
title_label.grid(row=8, column=0, columnspan=2, padx=5, pady=1)

# Создание горизонтальной черты на первой вкладке
separator = ttk.Separator(tab1, orient='horizontal')
separator.grid(row=9, columnspan=2, sticky='ew', padx=5, pady=1)

input_label = ttk.Label(tab1, text="Дата:")
input_label.grid(row=10, column=0, padx=5, pady=2)
input_entry5 = ttk.Entry(tab1)
input_entry5.grid(row=10, column=1, padx=5, pady=2)

citizenship_label = ttk.Label(tab1, text="Страна:")
citizenship_label.grid(row=11, column=0, padx=5, pady=2)
citizenship_combobox4 = ttk.Combobox(tab1, values=["РОССИЯ", "КАЗАХСТАН", "УЗБЕКИСТАН"])
citizenship_combobox4.grid(row=11, column=1, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Регион:")
input_label.grid(row=12, column=0, padx=5, pady=2)
input_entry6 = ttk.Entry(tab1)
input_entry6.grid(row=12, column=1, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Район:")
input_label.grid(row=13, column=0, padx=5, pady=2)
input_entry7 = ttk.Entry(tab1)
input_entry7.grid(row=13, column=1, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Город:")
input_label.grid(row=14, column=0, padx=5, pady=2)
input_entry8 = ttk.Entry(tab1)
input_entry8.grid(row=14, column=1, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Населенный пунк:")
input_label.grid(row=15, column=0, padx=5, pady=2)
input_entry9 = ttk.Entry(tab1)
input_entry9.grid(row=15, column=1, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Как в паспорте:")
input_label.grid(row=16, column=0, padx=5, pady=2)
input_entry10 = tk.Text(tab1, height=3, width=20)
input_entry10.grid(row=17, column=0, columnspan=2, sticky='ew', padx=5, pady=2)

# Создание заголовка на два столбца
title_label = ttk.Label(tab1, text="Дополнительно", font=("Arial", 10, "bold"))
title_label.grid(row=18, column=0, columnspan=2, padx=5, pady=2, sticky="s")

# Создание горизонтальной черты на первой вкладке
separator = ttk.Separator(tab1, orient='horizontal')
separator.grid(row=19, columnspan=2, column=0, sticky='ew', padx=5, pady=1)

input_label = ttk.Label(tab1, text="Телефон:")
input_label.grid(row=20, column=0, padx=5, pady=2)
input_entry9 = ttk.Entry(tab1)
input_entry9.grid(row=20, column=1, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Mail:")
input_label.grid(row=21, column=0, padx=5, pady=2)
input_entry9 = ttk.Entry(tab1)
input_entry9.grid(row=21, column=1, padx=5, pady=2)

# Создание заголовка на два столбца
title_label = ttk.Label(tab1, text="Документ", font=("Arial", 10, "bold"))
title_label.grid(row=0, column=2, columnspan=2, padx=5, pady=2, sticky="s")

# Создание горизонтальной черты на первой вкладке
separator = ttk.Separator(tab1, orient='horizontal')
separator.grid(row=1, columnspan=2, column=2, sticky='ew', padx=5, pady=1)

citizenship_combobox5 = ttk.Combobox(tab1, values=["ПАСПОРТ", "НЕ ПАСПОРТ"])
citizenship_combobox5.grid(row=2, column=2, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Серия:")
input_label.grid(row=3, column=2, padx=5, pady=2)
input_entry11 = ttk.Entry(tab1)
input_entry11.grid(row=3, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Номер:")
input_label.grid(row=4, column=2, padx=5, pady=2)
input_entry12 = ttk.Entry(tab1)
input_entry12.grid(row=4, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Кем выдан:")
input_label.grid(row=5, column=2, padx=5, pady=2)
input_entry13 = tk.Text(tab1, height=3, width=20)
input_entry13.grid(row=6, column=2, columnspan=2, sticky='ew', padx=5, pady=2)

input_label = ttk.Label(tab1, text="Код подразделения УФМС:")
input_label.grid(row=7, column=2, padx=5, pady=2)
input_entry14 = ttk.Entry(tab1)
input_entry14.grid(row=7, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Дата выдачи:")
input_label.grid(row=8, column=2, padx=5, pady=2)
input_entry15 = ttk.Entry(tab1)
input_entry15.grid(row=8, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Действует до:")
input_label.grid(row=9, column=2, padx=5, pady=2)
input_entry16 = ttk.Entry(tab1)
input_entry16.grid(row=9, column=3, padx=5, pady=2)


# Создание заголовка на второго столбца
title_label = ttk.Label(tab1, text="Регистрация по месту жительства", font=("Arial", 10, "bold"))
title_label.grid(row=10, column=2, columnspan=2, padx=5, pady=2, sticky="s")

# Создание горизонтальной черты на первой вкладке
separator = ttk.Separator(tab1, orient='horizontal')
separator.grid(row=11, columnspan=2, column=2, sticky='ew', padx=5, pady=1)

citizenship_combobox6 = ttk.Combobox(tab1, values=["жительства", "пребывания", "обращения"])
citizenship_combobox6.grid(row=12, column=2, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Регион:")
input_label.grid(row=13, column=2, padx=5, pady=2)
input_entry17 = ttk.Entry(tab1)
input_entry17.grid(row=13, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Район:")
input_label.grid(row=14, column=2, padx=5, pady=2)
input_entry18 = ttk.Entry(tab1)
input_entry18.grid(row=14, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Город:")
input_label.grid(row=15, column=2, padx=5, pady=2)
input_entry19 = ttk.Entry(tab1)
input_entry19.grid(row=15, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Район города:")
input_label.grid(row=16, column=2, padx=5, pady=2)
input_entry20 = ttk.Entry(tab1)
input_entry20.grid(row=16, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Нас. пункт:")
input_label.grid(row=17, column=2, padx=5, pady=2)
input_entry21 = ttk.Entry(tab1)
input_entry21.grid(row=17, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Улица:")
input_label.grid(row=18, column=2, padx=5, pady=2)
input_entry22 = ttk.Entry(tab1)
input_entry22.grid(row=18, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Дом:")
input_label.grid(row=19, column=2, padx=5, pady=2)
input_entry23 = ttk.Entry(tab1)
input_entry23.grid(row=19, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Корпус:")
input_label.grid(row=20, column=2, padx=5, pady=2)
input_entry24 = ttk.Entry(tab1)
input_entry24.grid(row=20, column=3, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Квартира:")
input_label.grid(row=21, column=2, padx=5, pady=2)
input_entry25 = ttk.Entry(tab1)
input_entry25.grid(row=21, column=3, padx=5, pady=2)

# Создание заголовка
title_label = ttk.Label(tab1, text="Прежняя или новая регистрация", font=("Arial", 10, "bold"))
title_label.grid(row=0, column=4, columnspan=2, padx=5, pady=2, sticky="s")

# Создание горизонтальной черты на первой вкладке
separator = ttk.Separator(tab1, orient='horizontal')
separator.grid(row=1, columnspan=2, column=4, sticky='ew', padx=5, pady=1)

citizenship_combobox7 = ttk.Combobox(tab1, values=["по месту жительства", "по месту пребывания"])
citizenship_combobox7.grid(row=2, column=4, padx=5, pady=2)

citizenship_label = ttk.Label(tab1, text="Страна:")
citizenship_label.grid(row=3, column=4, padx=5, pady=2)
citizenship_combobox5 = ttk.Combobox(tab1, values=["РОССИЯ", "КАЗАХСТАН", "УЗБЕКИСТАН"])
citizenship_combobox5.grid(row=3, column=5, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Улица:")
input_label.grid(row=4, column=4, padx=5, pady=2)
input_entry26 = ttk.Entry(tab1)
input_entry26.grid(row=4, column=5, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Дом:")
input_label.grid(row=5, column=4, padx=5, pady=2)
input_entry27 = ttk.Entry(tab1)
input_entry27.grid(row=5, column=5, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Корпус:")
input_label.grid(row=6, column=4, padx=5, pady=2)
input_entry28 = ttk.Entry(tab1)
input_entry28.grid(row=6, column=5, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Квартира:")
input_label.grid(row=7, column=4, padx=5, pady=2)
input_entry29 = ttk.Entry(tab1)
input_entry29.grid(row=7, column=5, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Регион:")
input_label.grid(row=8, column=4, padx=5, pady=2)
input_entry30 = ttk.Entry(tab1)
input_entry30.grid(row=8, column=5, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Район:")
input_label.grid(row=9, column=4, padx=5, pady=2)
input_entry31 = ttk.Entry(tab1)
input_entry31.grid(row=9, column=5, padx=5, pady=2)

input_label = ttk.Label(tab1, text="Город:")
input_label.grid(row=10, column=4, padx=5, pady=2)
input_entry32 = ttk.Entry(tab1)
input_entry32.grid(row=10, column=5, padx=5, pady=2)

# Создание заголовка
title_label = ttk.Label(tab1, text="Период регистрации", font=("Arial", 10, "bold"))
title_label.grid(row=11, column=4, columnspan=2, padx=5, pady=2, sticky="s")

# Создание горизонтальной черты на первой вкладке
separator = ttk.Separator(tab1, orient='horizontal')
separator.grid(row=12, columnspan=2, column=4, sticky='ew', padx=5, pady=1)

input_label = ttk.Label(tab1, text="с:")
input_label.grid(row=13, column=4, padx=5, pady=2)
input_entry33 = ttk.Entry(tab1)
input_entry33.grid(row=13, column=5, padx=5, pady=2)

input_label = ttk.Label(tab1, text="по:")
input_label.grid(row=14, column=4, padx=5, pady=2)
input_entry34 = ttk.Entry(tab1)
input_entry34.grid(row=14, column=5, padx=5, pady=2)

# Создание заголовка
title_label = ttk.Label(tab1, text="Для статталона", font=("Arial", 10, "bold"))
title_label.grid(row=0, column=6, columnspan=2, padx=5, pady=2, sticky="s")

# Создание горизонтальной черты на первой вкладке
separator = ttk.Separator(tab1, orient='horizontal')
separator.grid(row=1, columnspan=2, column=6, sticky='ew', padx=5, pady=1)

input_label = ttk.Label(tab1, text="Основное обстоятельство, вызвавшее необходимость переселения:")
input_label.grid(row=2, column=6, padx=5, pady=2)
input_entry35 = ttk.Entry(tab1)
input_entry35.grid(row=3, column=6, columnspan=2, sticky='ew', padx=5, pady=2)

input_label = ttk.Label(tab1, text="Вид занятий:")
input_label.grid(row=4, column=6, padx=5, pady=2)
input_entry36 = ttk.Entry(tab1)
input_entry36.grid(row=5, column=6, columnspan=2, sticky='ew', padx=5, pady=2)

input_label = ttk.Label(tab1, text="Уровень образования:")
input_label.grid(row=6, column=6, padx=5, pady=2)
input_entry37 = ttk.Entry(tab1)
input_entry37.grid(row=7, column=6, columnspan=2, sticky='ew', padx=5, pady=2)

input_label = ttk.Label(tab1, text="Семейное положение:")
input_label.grid(row=8, column=6, padx=5, pady=2)
input_entry38 = ttk.Entry(tab1)
input_entry38.grid(row=9, column=6, columnspan=2, sticky='ew', padx=5, pady=2)

input_label = ttk.Label(tab1, text="До переселения:")
input_label.grid(row=10, column=6, padx=5, pady=2)
input_entry39 = ttk.Entry(tab1)
input_entry39.grid(row=11, column=6, columnspan=2, sticky='ew', padx=5, pady=2)

input_label = ttk.Label(tab1, text="Статус занятости:")
input_label.grid(row=12, column=6, padx=5, pady=2)
input_entry40 = ttk.Entry(tab1)
input_entry40.grid(row=13, column=6, columnspan=2, sticky='ew', padx=5, pady=2)


# Запуск главного цикла обработки событий
root.mainloop()
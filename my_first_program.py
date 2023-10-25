import time


# Создаем декоратор, который будет считать время выполнения функции
def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы: {dt:.10f} сек")
        return res

    return wrapper


# Создаем декоратор, который будет добавлять текстовое оформление к функции
def decoration_text(func):
    def wrapper(*args):
        # Проверяем, является ли аргумент строкой
        if isinstance(args[0], str):
            # Возвращаем строку, содержащую имя, переданное в функцию
            return f'Меня зовут {args[0]}'
        else:
            return "***"

    return wrapper


# Декорируем функцию reading с помощью декоратора decoration_text
@decoration_text
def reading(text: str):
    return text


def get_age_text(age):
    """Функция, определяющая правильное склонение слова "год" в зависимости от возраста"""
    if isinstance(age, int):
        if age % 10 == 1 and age % 100 != 11:
            return "год"
        elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
            return "года"
        else:
            return "лет"
    else:
        return "***"


# testing1 и testing2 использую декоратор который добавляет текст "Меня зовут" к имени
# @test_time
def testing1():
    test_func = reading('Михаил')
    age = 33
    print(f'\n{test_func}, Мне {age} {get_age_text(age)}')


# @test_time
def testing2():
    test_func = reading(777)
    age = "много"
    print(f'\n{test_func}, Мне {age} {get_age_text(age)}')


# финальная версия
# @test_time
def testing3(name: str, age: int): # обьявляем фунцию с позиционными аргументами
    """Функция принемает на вход имя, и возраст, возвращает приветственный текст"""
    if isinstance(name, str) and isinstance(age, int): # проверяем аргументы что они соответствуют правильному типу
        test_func = reading(name) # используем декаратор для добавления "меня зовут"
        return print(f'\n{test_func}, Мне {age} {get_age_text(age)}') # возвращяем вывод информации
    else: # в случае не соответсвия типов данных воозвращаем соответствующие сообщение
        print("\nВведены неверные данные")

"""
testing1()
testing2()

testing3("Петр", 20)
testing3(123, "мало")


#                                                                                                           2 дз
#                                                                                                           2 дз
# def calculated(x, y, z):
#     if z == "+":
#         print(f"Результат: {x + y}")
#     else:
#         print(f"Результат: {x - y}")
#
#
# print(f"Привет! это простой калькулятор.\n"
#       f"Доступны операции: +, -")
#
# calculated(z=input("Выберите операцию: "),
#            x=float(input("Введите первое чиало: ")),
#            y=float(input("Введите второе чиало: ")))

__________________________________________________________________________v2


def calculated(x, y, z):
    if z == "+":
        print(f"Результат: {x + y}")
    elif z == "-":
        print(f"Результат: {x - y}")
    else:
        print("Некорректная операция. Пожалуйста, введите '+' или '-'.")


print(f"Привет! это простой калькулятор.\n"
      f"Доступны операции: +, -")

try:
    calculated(z=input("Выберите операцию: "),
               x=float(input("Введите первое число: ")),
               y=float(input("Введите второе число: ")))
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите числа.")


#                                                                                                           3 дз


def cinema_case(age: int, companion="нет"):
    if age < 12 and companion.lower() == "да":
        return "Билет бесплатный"
    elif 12 <= age < 18 and companion.lower() == "да":
        return "Билет со скидкой"
    elif age >= 18:
        return "Полная стоимость билета"
    else:
        return "Билет непродам"


print(cinema_case(age=int(input("Введите ваш возраст: ")), companion=input("Есть ли у вас сопровождающий? (да/нет): ")))
"""

#                                                                                                          4 дз


# def ages(year: int):
#    """программа, которая запрашивает у пользователя его возраст и выводит сообщение "Вы совершеннолетний(я)" или
#    "Вы несовершеннолетний(я)", в зависимости от значения возраста (18 и больше - совершеннолетие)."""
#     if year >= 18:
#         return "Вы совершеннолетний(я)"
#     elif year < 18:
#         if year in range(0, 18):
#             return "Вы несовершеннолетний(я)"
#         else:
#             return "хаха"
#
#
# print(ages(int(input("какой твой возраст "))))


# def greet_user():
#     """программу, которая запрашивает у пользователя его имя и выводит приветственное сообщение"""
#     name = input("Введите ваше имя: ")
#
#     if name and name.isalpha() and ' ' not in name:
#         print(f"Привет, {name}!")
#     else:
#         print("Вы не ввели корректное имя.")
#
#
# greet_user()


#                                                               5 дз Домашнее задание Списки

# Задание 1: Работа с списками и срезами

# my_list = ["apple", 123, True, "banana", 456, False, "orange", 789, True, 10.5]
#
# # Вывод списка на экран
# print(my_list)
#
# # Вывод первых 5 элементов списка
# print(my_list[:5])
#
# # Вывод последних 3 элементов списка
# print(my_list[-3:])
#
# # Вывод каждого второго элемента списка
# print(my_list[::2])
#
# # Изменение 3 элемента списка
# my_list[2] = "cherry"
#
# # Вывод измененного списка на экран
# print(my_list)


"""Работа с условиями и циклами

Попросите пользователя ввести число с клавиатуры. Если число делится на 3 без остатка, выведите сообщение
"Число делится на 3". Если число больше 10, выведите сообщение "Число больше 10". Если число не удовлетворяет
ни одному из условий, выведите сообщение "Число не соответствует условиям"."""

# number = int(input("Введите число: "))
#
# if number % 3 == 0:
#     print("Число делится на 3")
# elif number > 10:
#     print("Число больше 10")
# else:
#     print("Число не соответствует условиям")



#                                                                       6 дз Домашнее задание Циклы While и For
"""1 Задание. Код с использованием for:
Программа запрашивает у пользователя некоторое целое число, после чего использует цикл for, чтобы вывести на экран 
все числа от 0 до введенного числа включительно. Функция range(n + 1) возвращает последовательность чисел от 0 до n 
включительно. Значение i поочередно принимает каждое из чисел этой последовательности, и для каждого из них выполняется 
команда print(i)
"""

# number = int(input("Введите целое число: "))
#
# for i in range(number + 1):
#     print(i)


"""Задание. Код с использованием while:
Программа запрашивает у пользователя некоторое целое число, после чего использует while, чтобы вывести на экран все 
числа от 0 до введенного числа включительно.Переменная i инициализируется значением 0, а затем на каждой итерации цикла 
проверяется условие i <= n. Если оно выполнено, то на экран выводится текущее значение переменной i, после чего значение
 i увеличивается на 1. Цикл продолжается, пока i не станет больше n
"""

# number = int(input("Введите целое число: "))
#
# i = 0
# while i <= number:
#     print(i)
#     i += 1

#                                                                       7 дз Домашнее задание Структуры данных

"""Вводятся два списка чисел, числа вводятся вручную. 
Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.
"""
# # Ввод первого списка чисел
# list1 = input("Введите первый список чисел: ").split()
#
# # Ввод второго списка чисел
# list2 = input("Введите второй список чисел: ").split()
#
# # Преобразование элементов списков в целые числа
# list1 = [int(num) for num in list1]
# list2 = [int(num) for num in list2]
#
# # Создание множеств из списков
# set1 = set(list1)
# set2 = set(list2)
#
# # Вычисление пересечения множеств
# intersection = set1.intersection(set2)
#
# # Вывод количества пересечений
# print("Количество пересечений:", len(intersection))

#                                                                       8 дз Словари и Функции

# # Создание словаря и операции с ним
#
# # Создайте пустой словарь с именем my_dict
# my_dict = {}
#
# # Добавьте в словарь my_dict следующие элементы:
# #
# # Ключ "name" с соответствующим значением "John".
# # Ключ "age" с соответствующим значением 25.
# # Ключ "city" с соответствующим значением "New York".
# my_dict["name"] = "John"
# my_dict["age"] = 25
# my_dict["city"] = "New York"
#
# # Выведите на экран содержимое словаря my_dict
# print("Содержимое словаря my_dict:")
# for key, value in my_dict.items():
#     print(f"ключ: {key}, Значение: {value}")
#
# # Измените возраст в словаре my_dict на 26
# my_dict["age"] = 26
# # Добавьте ключ "email" со значением "john@example.com" в словарь my_dict
# my_dict["email"] = "john@example.com"
#
# # Проверьте, есть ли ключ "country" в словаре my_dict, и выведите соответствующее сообщение
# if "country" in my_dict:
#     print("Ключ 'country' есть в словаре my_dict")
# else:
#     print("Ключ 'country' отсутствует в словаре my_dict")
#
# # Выведите на экран все ключи и значения из словаря my_dict
# print("Все ключи и значения из словаря my_dict:")
# for key, value in my_dict.items():
#     print(f"ключ: {key}, Значение: {value}")

#                                                       9 дз Проект по автоматизации выполнении задач на собственном ПК

# import tkinter as tk
# from tkinter import messagebox
#
#
# def show_text():
#     text = entry.get()
#     messagebox.showinfo("Введенный текст", text)
#
#
# def clear_text():
#     entry.delete(0, tk.END)
#
# # Создание основного окна приложения
# root = tk.Tk()
# root['bg'] = "#fafafa" # зажний фон
# root.title('Название программы') # название программы
# root.wm_attributes('-alpha', 0.7) # прозрачность окна
# root.geometry('300x250') # размер окна
#
# # Добавление виджета Entry
# entry = tk.Entry(root)
# entry.pack()
#
# # Создание кнопки для отображения текста
# show_button = tk.Button(root, text="Показать текст", command=show_text)
# show_button.pack()
#
# # Создание кнопки для очистки поля ввода
# clear_button = tk.Button(root, text="Очистить", command=clear_text)
# clear_button.pack()
#
# # Запуск основного цикла обработки событий
# root.mainloop()

#                                                       10 дз Обзорная лекция

import tkinter as tk
import random

# Определения Python
definitions = {
    "While": "Цикл 'while' используется для выполнения блока кода, пока условие истинно.",
    "For": "Цикл 'for' используется для итерации по элементам последовательности (например, списку или строке).",
    "If": "Условие 'if' позволяет выполнить определенный блок кода, если условие истинно.",
    "Function": "Функция - это блок кода, который можно вызывать с определенными аргументами.",
    "List": "Список - это упорядоченная коллекция элементов, которая может содержать разные типы данных."
}


def show_random_definition():
    key = random.choice(list(definitions.keys()))
    definition_text.delete(1.0, tk.END)
    definition_text.insert(tk.END, key + " - это " + definitions[key])

# Создание главного окна
root = tk.Tk()
root.title("Определения Python")

# Создание заголовка
title_label = tk.Label(root, text="Определения Python", font=("Arial", 24))
title_label.pack()

# Создание текстового поля для определений
definition_text = tk.Text(root, width=50, height=5)
definition_text.config(font=("Arial", 16))
# definition_text.pack(side="top", anchor="center")

definition_text.pack()

# Создание кнопки "Показать определение"
show_def_button = tk.Button(root, text="Показать определение", command=show_random_definition)
show_def_button.pack()

# Запуск главного цикла приложения
root.mainloop()

import random
import string

# from random import sample

n = 8  # длина пароля по умолчанию


def get_random_password() -> str:
    lst_ = []  # создаю пустой список
    random_elements = string.ascii_letters + string.digits
    # рандомный эл-т = Конкатенации ascii_lowercase и ascii_uppercase константы  + численной строки
    for value in random.sample(random_elements, n):  # задаем цикл для рандомных эд-ов длинной 8
        lst_.append(value)  # расш. список несколькими значениями из любого вида нашей итерации

    return lst_


...  # TODO написать функцию генерации случайных паролей

print(get_random_password())

# str_ = ''.join(str_.split())

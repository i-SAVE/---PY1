# TODO решить с помощью list comprehension и распечатать его
import pprint

numbers = []  # создаю пустой список
min_num = 0  # минимальное число в списке
max_num = 15  # максимальное число в списке

for n in range(min_num, max_num + 1):  # для цикла от 0 - 15
    list_for_numbers = {"bin": bin(n), "dec": n, "hex": hex(n), "oct": oct(n)}
    # находим словари с помощью list comprehension
    numbers.append(list_for_numbers)
pprint.pprint(numbers)  # печатаем его

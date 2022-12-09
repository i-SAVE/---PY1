from random import sample

range_start = -10
range_end = 10
size_of_list = 15


def get_unique_list_numbers() -> list[int]:
    new_list = sample(range(range_start, range_end + 1), size_of_list)
    # создаем лист с рандомными числами и с уникальными знаяениями
    # sample - возвращает список уник. эл-ов длиной k, выбранных из последовательности заполнения.
    # Используется для случайной выборки без замены.
    return new_list


# 2 вариант решения данной проблемы (не лучший :( )

# def get_unique_list_numbers() -> list[int]:
#   new_list = []
#   while len(new_list) < size_of_list:
#      value = randint(range_start, range_end)
#     if value not in new_list:
#         new_list.append(value)
# return new_list

...  # TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

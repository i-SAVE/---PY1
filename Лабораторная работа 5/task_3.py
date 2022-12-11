from random import randint


def get_unique_list_numbers(length, min_value, max_value):
    new_list = []
    while len(new_list) < length:
        value = randint(min_value, max_value)
        if value not in new_list:
            new_list.append(value)
    return new_list


# выражаем функцию sample через этот код :)

...  # TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers(15, -10, 10)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

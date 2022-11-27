list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_res = 0
last_value = list_numbers[-1]
# TODO Оформить решение
for i in range(len(list_numbers)):  # перебираем все индксы
    max_value = list_numbers[max_res]  # присвоим переменной значение потенциального макс значения
    if list_numbers[i] >= max_value:  # если текущее значение больше max, переобозначим индекс максимального значения
        max_res = i

# поменяем местами последний элемент и последний макс элемент
list_numbers[-1] = list_numbers[max_res]
list_numbers[max_res] = last_value

print(list_numbers)

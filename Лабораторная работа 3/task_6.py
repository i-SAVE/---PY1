list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

max_index = 0  # предпологаем, что индекс max значения это "0"
last_index = -1  # обозначаем индекс послденего значения списка

max_number = list_numbers[max_index]  # предпологаю, что max значение это значение под max_index
last_value = list_numbers[last_index]  # выписываю посл. значение списка

for i, current_number in enumerate(list_numbers):
    # выписваю цикл с командой enumerate
    if current_number >= max_number:  # пишу условие - если текущее значение списка > или = max значения
        max_number = current_number  # (предпологаемого) - то я меняю его на текцщее в цикле (и значение и индекс)
        max_index = i
# получив максимальное знаяение перебрав весь список благодаря циклу и условию перейдем к смене мест значений

list_numbers[max_index], list_numbers[last_index] = list_numbers[last_index], list_numbers[max_index]
# используб множеств. присваивание, чтобы поменять местами max_number (макс.число и посл.число)
print(list_numbers)

# Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]

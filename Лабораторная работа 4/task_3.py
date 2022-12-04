# Вариант с использованнием встроенной функции - remove

def delete(list_, index=None):
    if index is None or "":  # если индекс - none
        list_.remove(list_[-1])  # убираем тогда последнюю строку
    else:
        list_.remove(index)  # в ином же случае убираем выбранный индекс
    return list_  # возвращаем переменную из функции в глоб. область


...  # TODO реализовать функцию удаления элемента из списка по индексу

print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]

def delete(list_, index=None):
    if index is not None and index >= 0:  # если индексу ничего не присвоили -none
        list_one = list_[index + 1:]
        list_two = list_[:index]  # разделяем с помощью слайсир. на 2
        list_two.extend(list_one)  # складываем значения без удаляемого
        return list_two
    if index is not None:
        del list_[index]
        return list_
    else:  # если индекс какое-то значение, то ищем послдений эл-нт
        return list_[:-1]


...  # TODO реализовать функцию удаления элемента из списка по индексу

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]

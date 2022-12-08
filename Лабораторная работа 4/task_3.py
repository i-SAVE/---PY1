def delete(list_, index=None):
    if index == -1 or index is None:  # если индексу ничего не присвоили -none или индекс -1
        del list_[-1]
        return list_
    else:
        list_one = list_[index + 1:]
        list_two = list_[:index]  # разделяем с помощью слайсир. на 2
        joined_list = [*list_two, *list_one]  # joined_list=list_two+list_one конкатенация списков
        return joined_list


...  # TODO реализовать функцию удаления элемента из списка по индексу

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]

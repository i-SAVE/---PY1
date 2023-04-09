def car_paths(n: int, m: int) -> list[list[int]] | int:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования

    matrix = [[1 for _ in range(m)] for _ in range(n)]  # Cоздадим базовую матрицу - с которой уже будем работать

    if n == 1 and m == 1:
        return 1
    elif n == 0 and m == 0:
        raise ValueError("Матрица пуста - к сожалению :(")
    elif m > 0 and n > 0:
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j] + matrix[i - 1][j - 1]
        return matrix


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7

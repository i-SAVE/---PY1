salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

for i in range(months):
    money_capital += spend - salary  # кол-во денег необходимое к концу 1 месяца
    spend += spend * 0.03  # находим ежемесяное увелеечние расходов на 0,03 каждый месяц со 2

print(round(money_capital))  # выводим и округляем результат решения

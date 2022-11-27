salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

for i in range(1, 11):
    if i == 1:  # расчет подушки безопаснсти для 1 месяца без повышения расходов
        money_capital += spend - salary
    else:
        money_capital += spend * 1.03 ** (i - 1) - salary  # условие для всех других месяцев

print(round(money_capital))

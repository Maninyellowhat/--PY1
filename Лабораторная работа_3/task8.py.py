money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
def life_lenth (money_capital, salary, spend, increase):
    month = 0
    while money_capital + salary >= spend:
        money_capital = money_capital - (spend-salary)
        spend += (spend*increase)
        month += 1
    print(month)

life_lenth (money_capital, salary, spend, increase)

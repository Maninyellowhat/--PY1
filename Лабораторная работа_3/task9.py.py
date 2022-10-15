salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

def money_safe(salary, spend, month, increase):
    need_money = spend - salary # количество денег, чтобы прожить 10 месяцев
    for i in range (1,months):
        spend += spend*increase
        need_money = need_money + (spend - salary)
    print(round(need_money))
money_safe(salary, spend, months, increase)

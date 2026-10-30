sales = {
    "Понедельник": [("капучино", 120, 14), ("латте", 150, 9), ("чай", 60, 21)],
    "Вторник":     [("капучино", 120, 8),  ("эспрессо", 90, 17), ("чай", 60, 12)],
    "Среда":       [("латте", 150, 11), ("эспрессо", 90, 6), ("какао", 110, 13)],
    "Четверг":     [("капучино", 120, 16), ("латте", 150, 7), ("чай", 60, 18)],
    "Пятница":     [("капучино", 120, 10), ("эспрессо", 90, 21), ("какао", 110, 9)],
}

def find_key(dict, value):
    for key, val in dict.items():
        if val == value:
            return key

def revenue (day):
    total_pon = 0
    for name, price, qty in day:
        total_pon += price * qty
    return f"Выручка {find_key(sales, day)}:{total_pon}"

def hit_day(day):
    best_pon = ""
    cnt_pon = 0
    for name, price, qty in day:
        if qty > cnt_pon:
            cnt_pon = qty
            best_pon = name
    return f"Хит {find_key(sales, day)}:{best_pon}"

for i in sales:
    print(revenue(sales[i]))
    print(hit_day(sales[i]))

def revenue_week (sales):
    rev, ma = 0, 0
    ans = []
    for i in sales:
        for name, price, qty in sales[i]:
            rev += price * qty
    return rev

print("итоговая выручка за неделю:", revenue_week(sales))

def aver_rev(sales):
    rev, ma = 0, 0
    ans = []
    for i in sales:
        for name, price, qty in sales[i]:
            rev += price * qty
        ans.append([rev,find_key(sales,sales[i])])
        rev = 0
    return max(ans)
print("день с максимальной выручкой:", aver_rev(sales)[1], aver_rev(sales)[0])

print("средняя выручка за день с округлением до рубля:", revenue_week(sales)//len(sales))
m = int(input("Введите стартовое кол-во организмов: "))
p = int(input("Введите среднесуточное увеличение в процентах: "))
n = int(input("Введите кол-во дней для размножения: "))
size_pop = m
for i in range(1, n + 1):
    size_pop += size_pop*float(f"0.{p}")
    print(f"""

Номер дня: {i}
Размер популяции: {size_pop}

""")

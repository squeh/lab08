digit = []
for i in range(10,0,-1):
    digit.append(int(input(f"Введите число, осталось ввести {i} раз: ")))
flag = "YES"
for i in digit:
    if i % 2 != 0:
        flag = "NO"
        break
print(flag)

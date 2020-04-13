# 6. В одномерном массиве найти сумму элементов, находящихся 
# между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

mas = [random.randint(0,20) for _ in range(10)]
print("Исходный массив: ")
print(mas)

# Находим минимум и максимум используя решение задачи 3
num_min = num_max = mas[0]
idx_max = idx_min = num = 0
for i in mas:
    if i > num_max:
        num_max = i
        idx_max = num
    elif i < num_min:
        num_min = i
        idx_min = num
    num+=1


print(f"Максимальный элемент: {num_max} на позиции {idx_max}. Минимальный: {num_min} на позиции {idx_min}")

# Если максимальный встретили раньше мнимального, просто поменяем местами индексы.
if idx_max < idx_min:
    idx_max, idx_min = idx_min, idx_max

result = 0

# Считаем сумму
for i in range(idx_min+1, idx_max):
    result+=mas[i]

print("Сумма: ")
print(result)
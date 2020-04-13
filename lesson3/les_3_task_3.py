# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.


import random

mas = [random.randint(0,100) for _ in range(50)]
print("Исходный массив: ")
print(mas)
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

mas[idx_min], mas[idx_max] = mas[idx_max], mas[idx_min]

print(f"Максимальный элемент: {num_max} на позиции {idx_max}. Минимальный: {num_min} на позиции {idx_min}")
print("Результирующий массив: ")
print(mas)
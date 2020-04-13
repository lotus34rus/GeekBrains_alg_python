# 5. В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве.

import random

mas = [random.randint(-10,100) for _ in range(50)]
print("Исходный массив: ")
print(mas)

i = 0
idx = -1
while i < len(mas) -1 :
        if mas[i] < 0 and idx == -1:
                idx = i
        elif mas[i] < 0 and mas[i] > mas[idx]:
                idx = i
        i += 1

print(f"Максимальный отрицательный элемент: {mas[idx]} на позиции {idx}")


# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные 
# цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input("Введите число: "))

sum = 0
sum2 = 0

while num != 0:
    tmp = num % 10
    if tmp % 2 == 0:
        sum+=1
    else:
        sum2+=1
    num = num // 10

print(f"Четных числел: {sum}")
print(f"Нечетных числел: {sum2}")

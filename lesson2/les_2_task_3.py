# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
# Например, если введено число 3486, надо вывести 6843.

num  = int(input("Введите число: "))
revers = ""

while num != 0:
    revers = "{0}{1}".format(revers, num % 10)
    num = num // 10

print(revers)

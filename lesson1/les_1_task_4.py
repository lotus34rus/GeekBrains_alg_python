# 4. Пользователь вводит две буквы.
#  Определить, на каких местах алфавита они стоят, 
#  и сколько между ними находится букв.

first = ord(input("Введите первую букву: "))
second = ord(input("Введите вторую букву: "))

first = first - ord('a') + 1
second = second - ord('a') + 1

print('Позиции: %d и %d' % (first,second))
print('Между буквами символов:', abs(first-second)-1)
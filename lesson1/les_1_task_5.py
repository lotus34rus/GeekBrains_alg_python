# 5. Пользователь вводит номер буквы в алфавите. 
# Определить, какая это буква.

a = int(input("Введите номер буквы: "))
a = ord('a') + a - 1

print(f"Это буква: {chr(a)}")
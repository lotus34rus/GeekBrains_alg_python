# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. 
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6

logical_and = a & b
logical_or = a | b
logical_xor = a ^ b
five_right =  a >> 2
five_left =  a << 2
 

print("Результат побитового OR: %10s" % logical_or)
print("Результат побитового AND: %10s" % logical_and)
print("Результат побитового XOR: %10s" % logical_xor)
print("Результат сдвига вправо: %10s" % five_right)
print("Результат сдвига влево XOR: %10s" % five_left)


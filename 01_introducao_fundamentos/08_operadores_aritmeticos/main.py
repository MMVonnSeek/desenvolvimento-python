a, b = 17, 5

print(a + b)   # 22 - adição
print(a - b)   # 12 - subtração
print(a * b)   # 85 - multiplicação
print(a / b)   # 3.4 - divisão (sempre float)
print(a // b)  # 3 - divisão inteira (descarta decimal)
print(a % b)   # 2 - módulo (RESTO da divisão)
print(2 ** 8)  # 256 - potenciação


# Precedência — igual à matemática
print(2 + 3 * 4)      # 14 (não 20!)
print((2 + 3) * 4)    # 20

# Operadores de atribuição
saldo = 1000
saldo += 500    # saldo = saldo + 500 → 1500
saldo -= 200    # 1300
saldo *= 2      # 2600
print(saldo)

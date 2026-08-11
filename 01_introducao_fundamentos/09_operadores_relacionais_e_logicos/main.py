x, y = 10, 7

print(x == y)   # False — igual a
print(x != y)   # True  — diferente de
print(x > y)    # True  — maior que
print(x < y)    # False — menor que
print(x >= 10)  # True  — maior ou igual
print(x <= 10)  # True  — menor ou igual


# Comparando strings
nome = 'Ana'
print(nome == 'Ana')   # True
print(nome == 'ana')   # False (case-sensitive!)


# Operadores lógicos: and, or, not
idade = 20
tem_carteira = True


# and: as DUAS condições precisam ser verdadeiras
pode_dirigir = idade >= 18 and tem_carteira
print(pode_dirigir)   # True


nota = 6.5
freq = 70


# or: PELO MENOS UMA precisa ser verdadeira
precisa_recuperar = nota < 7.0 or freq < 75
print(precisa_recuperar)   # True


# not: inverte
print(not True)    # False
print(not False)   # True

# Criando variáveis
# Variável é como um compartimento com etiqueta na mochila
# O = em python não significa igual, significa ATRIBUIÇÃO
nome = 'Max Muller'
idade = 35
altura = 1.76
estudante = True

print(nome)
print(idade)
print(altura)

# Atribuição múltipla
a, b, c = 1, 2, 3
print(a, b, c)

nome, idade, altura = 'Max Muller', 35, 1.76
print(nome, idade, altura)

# Troca elegante de valores
x = 10
y = 20
x, y = y, x
print(x, y)

# VÁLIDOS
nome_completo = "Max Muller"
_variavel = 19
salario2026 = 2500.90

# INVÁLIDOS
# 1nome = 'erro'
# nome completo = "Max Muller"
# for = 10
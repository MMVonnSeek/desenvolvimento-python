# Criando listas
frutas = ['maçã', 'banana', 'laranja', 'uva']

# ordena a lista
frutas.sort(reverse=True)

# imprime a lista na tela
for fruta in frutas:
    print(fruta)

# Acesso pelo índice
print(frutas[0]) # maçã
print(frutas[-1]) # uva (último)
print(len(frutas)) # 4

# Métodos básicos
frutas.append('manga')
frutas.remove('banana')
print(frutas)
print('laranja' in frutas)

# Percorrendo com for
for fruta in frutas:
    print(f' Fruta: {fruta}')
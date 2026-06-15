# Capturando texto
nome = input('Digite seu nome: ')
print(f'Olá,  {nome}')

# Capturando número - COM e SEM conversão
# SEM conversão (errado para calculo)
# idade = input('idade')
# print(idade + 1) # TypeError!

# COM conversão (correto):
idade = int(input('idade: '))
print(f'Você tem {idade} anos')
print(f'Em 10 anos terá {idade + 10} anos')

# float
altura = float(input('Altura em metros: '))
print(f'Sua altura: {altura:.2f}m')

# Constantes, conversão MAIÚSCULAS
PI = 3.14159
TAXA_IPI = 0.10
NOTA_MINIMA = 7.0
NOME_EMPRESA = 'SENAI'
print(f'Empresa: {NOME_EMPRESA}')
print(f'Nota mínima para aprovação: {NOTA_MINIMA}')

# Validação simples com loop
# Exemplo para idade
while True:
    entrada = input('Digite sua idade:')
    if entrada.isdigit():
        idade = int(entrada)
        break
    else:
        print('Erro! Digite apenas números para idade')

    print(f'Sua idade é {idade}')
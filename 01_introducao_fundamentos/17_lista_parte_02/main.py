notas = []
n = int(input('Quantas notas? '))

for i in range(n):
    nota = float(input(f'Nota {i+1}: '))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f'Notas: {notas}')
print(f'Média: {media:.2f}')
print(f'Maior: {max(notas)} Menor: {min(notas)}')
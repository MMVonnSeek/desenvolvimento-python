# if / elif / else — múltiplas condições
nota = float(input('Nota do aluno: '))


if nota >= 9.0:
    conceito = 'A'
    situacao = 'Excelente'
elif nota >= 7.0:
    conceito = 'B'
    situacao = 'Aprovado'
elif nota >= 5.0:
    conceito = 'C'
    situacao = 'Recuperação'
else:
    conceito = 'D'
    situacao = 'Reprovado'


print(f'Conceito: {conceito} | Situação: {situacao}')

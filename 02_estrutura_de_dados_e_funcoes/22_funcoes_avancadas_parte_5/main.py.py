# DEPOIS: código refatorado com funções
NOTA_MINIMA = 7.0

def coletar_dados(numero):
    """Coleta nome e notas de um aluno."""
    nome = input(f'Nome do aluno {numero}: ')
    p1 = float(input(' Nota P1: '))
    p2 = float(input(' Nota P2: '))
    return nome, p1, p2

def calcular_situacao(p1, p2):
    """Retorna média e situação do aluno."""
    media = (p1+p2)/2
    sit = 'Aprovado' if media >= NOTA_MINIMA else 'Reprovado'
    return media, sit

def exibir_resultado(nome, media, sit):
    print(f'{nome}: {sit} (média {media:.2f})')

# Programa principal — agora escalável para qualquer número de alunos
n = int(input('Quantos alunos? '))
for i in range(1, n+1):
    nome, p1, p2 = coletar_dados(i)
    media, sit = calcular_situacao(p1, p2)
    exibir_resultado(nome, media, sit)
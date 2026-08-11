# Mini-planilha de notas da turma
nomes  = ['Ana','Bruno','Carlos','Diana','Eduardo']
notas1 = [8.5, 7.0, 9.2, 6.8, 10.0]
notas2 = [7.5, 8.0, 8.8, 5.5,  9.5]

# Exibe tabela formatada com zip e enumerate
print(f"{'Nº':<4} {'Nome':<12} {'P1':>5} {'P2':>5} {'Média':>7} {'Sit.':<12}")
print('-' * 45)

for i,(nome,n1,n2) in enumerate(zip(nomes,notas1,notas2),start=1):
    media = (n1+n2)/2
    sit = 'Aprovado' if media >= 7.0 else 'Reprovado'
    print(f'{i:<4} {nome:<12} {n1:>5.1f} {n2:>5.1f} {media:>7.2f} {sit:<12}')

# Estatísticas usando list comprehension básica
medias = [(n1+n2)/2 for n1,n2 in zip(notas1,notas2)]
print(f'\nMédia geral: {sum(medias)/len(medias):.2f}')
print(f'Melhor nota: {max(medias):.2f}')
print(f'Aprovados:   {sum(1 for m in medias if m >= 7.0)} de {len(nomes)}')

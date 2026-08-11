# Lambda básico
dobrar = lambda x: x * 2
print(dobrar(5)) # 10

# sorted com key lambda
alunos = [('Ana',9.0),('Carlos',6.5),('Bruno',8.0)]
por_nota = sorted(alunos, key=lambda a: a[1], reverse=True)
for nome, nota in por_nota:
    print(f'{nome}: {nota}')

# map e filter
notas = [4.5, 7.0, 8.5, 3.0, 9.2]
aprov = list(filter(lambda n: n >= 7.0, notas))
dobr = list(map(lambda n: round(n*2,1), notas))
print(aprov)
print(dobr)
aluno = {} # vazio
aluno['nome'] = 'Carlos'
aluno['idade'] = 17
aluno['nota'] = 8.5
print(aluno)

# Forma compacta
aluno2 = {'nome':'Alice', 
          'Idade':18,
          'nota':9.0}

print(aluno.get('nome'))
print(aluno.get('email')) # None - sem erro
print(aluno.get('email', 'N/A')) # Valor padrão

# Percorrendo
for chave, valor in aluno.items():
    print(f'{chave}:{valor}')
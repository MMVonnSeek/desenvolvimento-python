# Lista de Dicionarios
produtos = [
    {'nome':'Notebook','preco':3500.0,'categoria':'eletronico'},
    {'nome':'Mouse', 'preco':89.9, 'categoria':'eletronico'},
    {'nome':'Cadeira', 'preco':650.0, 'categoria':'mobilia'},
]

# Filtrar
eletronic = [p for p in produtos if p['categoria']=='eletronico']
print(len(eletronic))

# Ordenar por preço
ordem = sorted(produtos, key=lambda p: p['preco'])
for p in ordem:
    print(f'{p['nome']} R$ {p['preco']:.2f}')

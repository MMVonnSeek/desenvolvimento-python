# dicionário
usuario = dict(
    nome="Max Muller", 
    idade=35, 
    email="max@gmail.com"
)

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
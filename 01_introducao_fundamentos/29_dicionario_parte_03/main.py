# dicionário
usuario = {
    'nome': "Max Muller",
    'idade': 35,
    'email': "max@gmail.com",
    'profissão': "programador"
}

# exibe os valores
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
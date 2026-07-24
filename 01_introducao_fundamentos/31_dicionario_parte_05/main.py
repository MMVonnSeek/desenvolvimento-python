# dicionário
usuario = {
    'nome': "Max",
    'idade': 35,
    'email': "max@gmail.com"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

# adicionando nova chave
usuario['profissão'] = input("Informe a profissão: ").strip()

print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
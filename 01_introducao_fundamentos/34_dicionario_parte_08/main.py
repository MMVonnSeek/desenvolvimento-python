chaves = ("Nome", "Idade", "E-mail", "Telefone", "Profissão")
usuario = {
    chaves[0]: "Max Muller",
    chaves[1]: 35,
    chaves[2]: "max@gmail.com",
    chaves[3]: "(61) 99999-9999",
    chaves[4]: "programador"
}

for chave in chaves:
    print(f"{chave}: {usuario.get(chave)}")
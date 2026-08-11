turma = {
    'Alice': {'nota': 9.0, 'frequencia': 90},
    'Bruno': {'nota':6.5, 'frequencia': 80},
    'Carlos': {'nota': 4.0, 'frequencia': 60},
}

# Acesso aninhado
print(turma['Alice']['nota'])
print(turma['Carlos']['frequencia'])

# Percorrendo e tomando decisão
for nome, dados in turma.items():
    ok = dados['nota'] >= 7.0 and dados['frequencia'] >= 75
    print(f'{nome}: {'Aprovado' if ok else 'Reprovado'}')
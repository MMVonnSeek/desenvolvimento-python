# Escopo de variáveis
def minha_funcao():
    variavel_local = 'Só existo aqui dentro'
    print(variavel_local) # funciona

minha_funcao()
# Print(variavel_local)  # NameError - não existe aqui

# Variável global
mensagem = 'Sou global'

def outra_funcao():
    print(mensagem) # pode ler variável global

outra_funcao()













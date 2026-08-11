# *args
def somar(*nums):
    return sum(nums)
print(somar(1,2)) #3
print(somar(1,2,3,4,5)) # 15
print(somar(10)) # 10

# **kwargs
def cadastrar(**dados):
    for k, v in dados.items():
        print(f'{k}: {v}')

cadastrar(nome='Ana', idade=17, curso='Python')

# Combinando fixo + *args + **kwargs
def relatorio(titulo, *itens, **config):
    sep = config.get('sep', '-')
    larg = config.get('larg', 30)
    print(sep*larg)
    print(titulo.center(larg))
    print(sep*larg)
    for item in itens:
        print(f' {item}')
relatorio('Notas', 'Ana: 9', 'Bruno: 7', sep='=', larg=25)
# Caso prático: senha com tentativas
SENHA = 'senai2026'
tentativas = 0
MAX = 3

while tentativas < MAX:
    senha = input('Senha: ')
    tentativas += 1

    if senha == SENHA:
        print('Acesso concedido!')
        break
    else:
        restantes = MAX - tentativas
        if restantes > 0:
            print(f'{restantes} tentativa(s) restante(s).')
if tentativas == MAX and senha != SENHA:
    print('Conta bloqueada.')
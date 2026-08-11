# ANTES: código sem funções — tudo misturado 
nome1 = input('Nome 1: ') 
n1_p1 = float(input('Nota P1: ')) 
n1_p2 = float(input('Nota P2: ')) 
media1 = (n1_p1+n1_p2)/2 
if media1 >= 7.0: 
    print(f'{nome1}: Aprovado ({media1:.2f})') 
else: 
    print(f'{nome1}: Reprovado ({media1:.2f})') 
 
nome2 = input('Nome 2: ') 
n2_p1 = float(input('Nota P1: ')) 
n2_p2 = float(input('Nota P2: ')) 
 
 
media2 = (n2_p1+n2_p2)/2 
if media2 >= 7.0: 
    print(f'{nome2}: Aprovado ({media2:.2f})') 
else: 
    print(f'{nome2}: Reprovado ({media2:.2f})') 

    
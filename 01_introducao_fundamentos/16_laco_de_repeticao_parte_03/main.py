# Loop for e range()
# range() — formas de usar
for i in range(5): # 0,1,2,3,4
    print(i, end=' ')
print()
for i in range(1, 6): # 1,2,3,4,5
    print(i, end=' ')
print()

for i in range(0, 11, 2): # 0,2,4,6,8,10
    print(i, end=' ')
print()
for i in range(10, 0, -1): # contagem regressiva
    print(i, end=' ')
print()


# break e continue
# break — para o loop
for n in range(1, 11):
    if n == 6:
        print('Achei o 6! Parando.')
    break
print(n, end=' ')
print()

# continue — pula a iteração atual
for n in range(1, 11):
    if n % 2 == 0: # pula pares
        continue
print(n, end=' ')

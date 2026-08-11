def fatorial(n):
    if n <= 1: # caso base
        return 1
    return n * fatorial(n - 1) # chamada recursiva
print(fatorial(5)) # 120
print(fatorial(0)) # 1
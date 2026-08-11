# 1. Nomes descritivos
# Ruim:
def calc(a, b):
    return a * b / 100

# Bom:
def calcular_percentual(valor_total, percentual):
    return valor_total * percentual / 100

# 2. Constantes em MAIÚSCULAS
NOTA_MINIMA    = 7.0
FREQUENCIA_MIN = 0.75

# 3. Espaços ao redor de operadores
x = 10 + 5    # correto
# x=10+5      # evitar

# 4. Docstring
def calcular_media(notas):
    """Retorna a média aritmética de uma lista de notas."""
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)
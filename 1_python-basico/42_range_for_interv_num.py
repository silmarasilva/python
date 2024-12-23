"""
For + Range
range -> range(start, stop, step)
"""

# O range em Python é uma função embutida usada para gerar uma sequência de números. 
# Ele é comumente usado em loops for para iterar sobre uma sequência de valores.

# Sintaxe
# A função range tem três formas principais de uso:

# range(stop)
# Gera números de 0 até stop - 1.

# range(start, stop)
# Gera números de start até stop - 1.

# range(start, stop, step)
# Gera números de start até stop - 1, com incrementos ou decrementos definidos por step.

# Parâmetros
# start (opcional): O valor inicial da sequência. Padrão é 0.
# stop: O valor onde a sequência para (não inclusivo).
# step (opcional): O incremento (ou decremento, se negativo) entre os números. Padrão é 1.


# EXEMPLOS:

# Apenas stop
for i in range(5):  # Gera números de 0 a 4
    print(i)

# Saída:
# 0
# 1
# 2
# 3
# 4


# start e stop
for i in range(2, 6):  # Gera números de 2 a 5
    print(i)

# Saída:
# 2
# 3
# 4
# 5

# start, stop e step
for i in range(1, 10, 2):  # Gera números de 1 a 9, pulando de 2 em 2
    print(i)

# Saída:
# 1
# 3
# 5
# 7
# 9

# Decremento com step negativo
for i in range(10, 0, -2):  # Gera números de 10 a 1, pulando de 2 em 2
    print(i)

# Saída:
# 10
# 8
# 6
# 4
# 2

# Usando range fora do loop
# O range não gera uma lista diretamente; ele cria um objeto iterável. 
# Se você quiser uma lista com os números, use a função list() para converter:

numeros = list(range(5))  # Converte o range em uma lista
print(numeros)
# Saída: [0, 1, 2, 3, 4]




# Curiosidades e comportamento
# range não inclui o stop
# Isso porque o stop é não inclusivo, como é comum em Python.
# step pode ser qualquer valor diferente de 0

# Pode ser positivo, negativo ou fracionado (se você usar bibliotecas externas como NumPy).


# Iteração reversa
# Se você quiser iterar em ordem decrescente, basta definir um step negativo:

for i in range(5, -1, -1):  # De 5 a 0
    print(i)

# O range não armazena todos os números na memória. 
# Ele calcula os valores sob demanda, o que o torna eficiente em termos de uso de memória.

# Usando range para calcular a soma dos números de 1 a 10:
soma = 0
for i in range(1, 11):  # De 1 a 10
    soma += i

print(f"A soma de 1 a 10 é: {soma}")
# Saída: A soma de 1 a 10 é: 55


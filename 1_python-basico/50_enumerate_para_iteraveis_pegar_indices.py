"""
enumerate - enumera iteráveis (índices)
"""


# O enumerate em Python é uma função útil para iterar sobre um iterável (como listas, tuplas, etc.) enquanto você acompanha os índices de cada elemento. Ele retorna um objeto iterável de tuplas, onde cada tupla contém:
# O índice do elemento.
# O valor do elemento correspondente.

# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# 0 Maria Maria
# 1 Helena Helena
# 2 Luiz Luiz
# 3 João João

lista = ['Maria', 'Helena', 'Luiz']
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

# 0 Maria
# 1 Helena
# 2 Luiz

lista = ['Maria', 'Helena', 'Luiz']
for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

# FOR da tupla:
#         0
#         Maria
# FOR da tupla:
#         1
#         Helena
# FOR da tupla:
#         2
#         Luiz
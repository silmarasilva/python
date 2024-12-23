"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# Métodos úteis:
#APPEND
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista.append(42)  # Adiciona 42 ao final da lista
print(lista)      # [123, True, 'Luiz Otávio', 1.2, [], 42]

# INSERT
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista.insert(1, 'Novo valor')  # Insere 'Novo valor' na posição 1
print(lista)                   # [123, 'Novo valor', True, 'Luiz Otávio', 1.2, [], 42]

# POP
lista = [123, True, 'Maria',  1.2, []]
elemento = lista.pop(2)  # Remove o elemento na posição 2
print(elemento)          # True
print(lista)             # [123, True, 1.2, []]

# DEL
lista = [123, True, 'Maria',  1.2, []]
del lista[0]  # Remove o primeiro elemento
print(lista)   # [True, 'Maria', 1.2, []]

#CLEAR
lista = [123, True, 'Maria',  1.2, []]
print(lista)   # [True, 'Maria', 1.2, []]
lista.clear()  # Limpa todos os dados da lista
print(lista)   # []

# Concatenando listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)  # [1, 2, 3, 4, 5, 6]

#EXTEND
# Aqui é importante entender que o extend irá alterar a lista A, inserindo os dados da B. 
lista_a = [1, 2, 3]
lista_b = [5, 6, 7]
lista_a.extend(lista_b)
print(lista_a)  # [1, 2, 3, 5, 6, 7]
print(lista_b)  # [5, 6, 7]
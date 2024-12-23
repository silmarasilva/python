# Desempacotamento em chamadas
# de métodos e funções

# O que é desempacotamento?
# Em Python, desempacotamento se refere a "desempacotar" ou "expandir" os elementos de uma estrutura (como uma lista, tupla ou string) para passá-los como argumentos individuais em uma função ou método.

# Desempacotamento básico:
# Imagine uma lista de elementos que você quer passar como parâmetros para uma função ou método. Em vez de passar a lista inteira, você pode usar o * para "desempacotar" os elementos dessa lista. Isso acontece principalmente em funções, para garantir que os argumentos sejam passados separadamente.


# Desempacotamento de uma lista:

lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
print(*lista) # Maria Helena 1 2 3 Eduarda

# Desempacotamento de uma string:

string = 'ABCD'
print(*string) # A B C D


tupla = 'Python', 'é', 'legal'
print(*tupla) # Python é legal


# Usando * em chamadas de funções com argumentos variáveis:
# Você pode usar o desempacotamento em funções que aceitam um número variável de argumentos. Isso é útil quando você não sabe quantos argumentos serão passados. O operador *args permite capturar qualquer número de argumentos posicionais.

def exemplo(*args):
    print(args) # ('Maria', 'Helena', 1, 2, 3, 'Eduarda')

exemplo('Maria', 'Helena', 1, 2, 3, 'Eduarda')

# Desempacotamento em uma lista de listas (exemplo com salas):
salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda'],
]

print(*salas, sep='\n')

# ['Maria', 'Helena']
# ['Elaine']
# ['Luiz', 'João', 'Eduarda'


# Desempacotamento em atribuições
# O desempacotamento também é útil quando você precisa desempacotar valores diretamente para variáveis.

# Desempacotamento com uma lista
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
p, b, *_, ap, u = lista  # Desempacota os valores da lista em variáveis
print(p, u, ap)  # Maria Eduarda 3

# A linha p, b, *_, ap, u = lista desempacota os valores de lista:
# p = 'Maria'
# b = 'Helena'
# *_, armazena os elementos intermediários (1, 2), mas não os usa (só ignora).
# ap = 'Eduarda'
# u = 3
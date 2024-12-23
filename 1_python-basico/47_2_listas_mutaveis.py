# Tipo list
# Mutável: Você pode alterar seus valores diretamente após a criação.
# Armazena vários valores: Uma lista pode conter elementos de qualquer tipo de dado, incluindo números, strings, booleanos, e até outras listas.


lista = [123, True, 'Luiz Otávio',  1.2, []]
# Modificando um elemento da lista:
lista[-3] = 'Maria'  # Substitui 'Luiz Otávio' por 'Maria'
print(lista)         # [123, True, 'Maria', 1.2, []]


# Acessando e verificando o tipo de um elemento:
lista = [123, True, 'Luiz Otávio',  1.2, []]
print(lista[2], type(lista[2]))  # ''Luiz Otávio' <class 'str'>


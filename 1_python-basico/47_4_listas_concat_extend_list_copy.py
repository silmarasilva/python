
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


"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# Resumo

# Em Python, o comportamento de atribuição e cópia varia dependendo do tipo de dado. 
# Vamos analisar cada exemplo e entender como isso funciona

# A atribuição em Python cria uma cópia da referência ao valor.
# Após a cópia, mudar o valor de uma variável não afeta a outra.
# Assim, outra_variavel continua com o valor 'Silmara', mesmo depois

# Strings (Valores Imutáveis) - Cria uma nova referência ao valor.

nome = 'Silmara'
outra_variavel = nome
nome = 'Eliza'

print(nome)             # Eliza
print(outra_variavel)   # Silmara

# Listas (Valores Mutáveis) - Compartilha a mesma referência.

lista_a = ['Luiz', 'Maria']
lista_b = lista_a
lista_a[0] = 'Qualquer coisa'
print(lista_a) # ['Qualquer coisa', 'Maria']
print(lista_b) # ['Qualquer coisa', 'Maria']


# COPY
# Usando .copy() para Listas ( Mutáveis) - Cria uma nova lista independente.
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()
lista_a[0] = 'Qualquer coisa'
print(lista_a) # ['Qualquer coisa', 'Maria', 1, True, 1.2]
print(lista_b) # ['Luiz', 'Maria', 1, True, 1.2]
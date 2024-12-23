"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print('Olha meu print aqui')


# Verifica se 5 é maior que 3
if 5 > 3:
    print("5 é maior que 3")

# Verifica se 10 é maior ou igual a 10
if 10 >= 10:
    print("10 é maior ou igual a 10")

# Verifica se 7 é menor que 10
if 7 < 10:
    print("7 é menor que 10")

# Verifica se 7 é menor que 10
if 7 < 10:
    print("7 é menor que 10")

# Verifica se 8 é menor ou igual a 8
if 8 <= 8:
    print("8 é menor ou igual a 8")

# Verifica se a string 'Python' é igual a 'Python'
if "Python" == "Python":
    print("As strings são iguais")

# Verifica se 20 é diferente de 15
if 20 != 15:
    print("20 é diferente de 15")


# Saída: 
"""
5 é maior que 3
10 é maior ou igual a 10
7 é menor que 10
8 é menor ou igual a 8
As strings são iguais
20 é diferente de 15
"""
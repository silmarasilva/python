"""
Introdução ao empacotamento e desempacotamento
"""

# Empacotamento
# O empacotamento ocorre quando você agrupa múltiplos valores em uma única variável, geralmente em uma tupla.
# Aqui, valores é uma tupla que contém os elementos (1, 2, 3, 4, 5).
# O empacotamento acontece automaticamente quando você atribui múltiplos valores sem usar colchetes ou parênteses explícitos.

valores = 1, 2, 3, 4, 5  # Os valores são empacotados em uma tupla
print(valores)  # (1, 2, 3, 4, 5)

# Desempacotamento
# O desempacotamento permite extrair os valores de uma estrutura (como listas ou tuplas) e atribuí-los a múltiplas variáveis.

# Usando Tuplas
a, b, c = 10, 20, 30  # Desempacota os valores da tupla
print(a)  # 10
print(b)  # 20
print(c)  # 30

# Usando Listas
# Regra Importante: O número de variáveis deve corresponder ao número de elementos na estrutura.

numeros = [1, 2, 3]
x, y, z = numeros  # Desempacota a lista
print(x, y, z)  # 1 2 3


nomes = ['Maria', 'Helena', 'Joao']
nome1, nome2, nome3 = nomes
print(nome2)  # Helena


nome1, nome2, nome3 = ['Maria', 'Helena', 'Joao']
print(nome2)  # Helena

nome1, nome2 = ['Maria', 'Helena', 'Joao']
print(nome2)  # ValueError: too many values to unpack (expected 2)

nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Joao']
print(nome2)  # ValueError: not enough values to unpack (expected 4, got 3)

# Resto (*) no Desempacotamento
# O operador * (asterisco) permite capturar o "resto" dos valores ao desempacotar, transformando-os em uma lista.

nome1, *resto = ['Maria', 'Helena', 'Joao']
print(nome1)  # Maria

*a, b = 1, 2, 3, 4, 5  # Captura todos os valores exceto o último em 'a'
print(a)  # [1, 2, 3, 4]
print(b)  # 5

a, *meio, b = 1, 2, 3, 4, 5  # Captura o primeiro e o último valor, e o meio vai para 'meio'
print(a)    # 1
print(meio) # [2, 3, 4]
print(b)    # 5

nome2, *resto = ['Maria', 'Helena', 'Joao']
print(nome1)  # NameError: name 'nome1' is not defined. Did you mean: 'nome2'?

nome1, *resto = ['Maria', 'Helena', 'Joao']
print(nome1, resto)  # Maria ['Helena', 'Joao']

nome1, *_ = ['Maria', 'Helena', 'Joao']
print(nome1)  # Maria 

_, nome2, *_ = ['Maria', 'Helena', 'Joao']
print(nome2)  # Helena 

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome) # Luiz 


# Empacotamento/Desempacotamento com Funções
# O empacotamento e desempacotamento são úteis em funções, especialmente quando você precisa trabalhar com listas ou dicionários.

# Com Listas (*args):
def soma(*numeros):
    return sum(numeros)
print(soma(1, 2, 3, 4))  # 10


# Com Dicionários (**kwargs):
def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
mostrar_dados(nome="Silmara", idade=37)
# nome: Silmara
# idade: 37
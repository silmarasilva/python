# Tipo list
# Acessível por índices: Permite acessar, modificar e excluir elementos usando índices ou fatiamento.

# Índices e Fatiamento:

string = 'ABCDE'  # String de 5 caracteres
print(string[0])  # Acessando o primeiro caractere (A)
print(string[-1]) # Acessando o último caractere (E)


# Índices positivos começam do 0 (da esquerda para a direita).
#        0    1      2              3    4
lista = [123, True, 'Luiz Otávio',  1.2, []]


# Índices negativos começam de -1 (da direita para a esquerda).
#       -5   -4       -3            -2   -1
lista = [123, True, 'Luiz Otávio', 1.2, []]


# A função len() retorna o número de elementos na lista.
# Exemplo com a função len()

frutas = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']
print(len(frutas))  # Retorna o número de elementos na lista: 5



# Fatiamento permite acessar subconjuntos da lista:

# Exemplo de fatiamento:

# # lista[início:fim:passo]
# início: índice inicial (inclusivo)
# fim: índice final (exclusivo)
# passo: quantos elementos "pular" (opcional)

# Acessando do índice 1 ao 3
frutas = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']
print(frutas[1:3])  # ['banana', 'laranja']

# Acessando do índice 2 até o final
frutas = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']
print(frutas[2:])  # ['laranja', 'uva', 'abacaxi']

# Acessando até o índice 3 (exclusivo)
frutas = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']
print(frutas[:3])  # ['maçã', 'banana', 'laranja']

# Acessando com passo. 
# Início: Não especificado, então o padrão é 0 (início da lista).
# Fim: Não especificado, então o padrão é o final da lista.
# Passo: 2, significa que a lista será percorrida pulando 1 elemento entre cada valor selecionado.

frutas = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']
print(frutas[::2])  # ['maçã', 'laranja', 'abacaxi'] (elementos alternados)

# Acessando de trás para frente
frutas = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']
print(frutas[::-1])  # ['abacaxi', 'uva', 'laranja', 'banana', 'maçã']

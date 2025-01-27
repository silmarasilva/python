"""

First-Class Functions
Funções de First-Class são funções tratadas como qualquer outro tipo de dado, como números, strings, listas, etc. Ou seja, você pode atribuí-las a variáveis, passá-las como argumentos para outras funções e retorná-las de funções.

"""

# Função atribuída a uma variável
soma = lambda a, b: a + b

# Usando a função atribuída
print(soma(2, 3))  # Output: 5

# Aqui, soma é uma função que foi atribuída a uma variável, o que mostra que as funções podem ser tratadas como objetos.

# Higher Order Functions
# Funções Higher-Order são aquelas que podem receber outras funções como argumentos ou retornar funções como resultado. Elas operam em outras funções, seja como entrada ou saída.

# Função que recebe outra função como argumento
def aplicar(func, x, y):
    return func(x, y)

# Passando a função soma como argumento
print(aplicar(lambda a, b: a + b, 2, 3))  # Output: 5

"""
Aqui, a função aplicar recebe outra função como argumento (no caso, uma função anônima lambda) e a utiliza para calcular o resultado. A função lambda é uma maneira de criar funções anônimas, ou seja, funções sem nome. Elas são muito úteis quando você precisa de uma função simples para usar uma única vez, sem a necessidade de defini-la formalmente com o comando def. lambda argumentos: expressão. argumentos: são os parâmetros da função (assim como em uma função normal).expressão: é o corpo da função, que deve retornar um valor.

"""

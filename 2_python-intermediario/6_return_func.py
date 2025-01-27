"""
Retorno de valores das funções (return)

O comando return em Python é usado para especificar o valor que uma função deve devolver após ser executada. 
Quando o Python encontra um return, ele:
- Interrompe a execução da função naquele ponto.
- Devolve o valor especificado após o return para quem chamou a função.

"""

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y

"""
A função soma recebe dois argumentos, x e y, e funciona assim:
Se o valor de x for maior que 10, ela devolve a lista [10, 20].
Caso contrário, devolve a soma de x + y.
"""

soma1 = soma(2, 2) # valor "4" é armazenado na variável "soma1"
soma2 = soma(3, 3) # valor "6" é armazenado na variável "soma1"
print(soma1)
print(soma2)
print(soma(11, 55))
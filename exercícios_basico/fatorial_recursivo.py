# Problema: Calcule o fatorial de um número usando recursão.

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))  # 120

'''
O fatorial de um número natural n, representaod por n! é o produto de todos os números inteiros de 1 até n.
Ou Seja, n! = n x ( n - 1 ) x (n - 2 ) x ... x 2 x 1.
Por exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120

'''
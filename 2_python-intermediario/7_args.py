'''
Args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''

# def soma(*args):
#     total = 0
#     for numero in args:
#         print ("Total", total, numero)
#         total = total + numero
#         print ("Total", total)

# soma(2,4,6)

# Total 0 2
# Total 2
# Total 2 4
# Total 6
# Total 6 6
# Total 12

# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero
#         print (total)


# soma(2,4,6)

# 2
# 6
# 12

# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero
#         # print (total)
#     return total

# resultado_soma = soma(2,4,6)
# print (resultado_soma)

# 12


# Usando a funcão SUM

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


print (sum((2,4,6)))


# A função `sum()` exige um único argumento iterável, como uma tupla. 
# Os parênteses internos criam a tupla `(2, 4, 6)`, 
# enquanto os externos são usados para chamar a função com esse argumento.

# Empacotamento vs Desempacotamento "*""
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

numeros = 2, 4, 6
resultado_soma = soma (*numeros)
print (resultado_soma)

# *args empacota o que é enviado para a funcao dentro de uma tupla. mas em resultado_soma = soma(*numeros) estamos desempacotando para enviar para a funcao.
'''
Exercícios com Funcões

Crie uma funcao que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.

'''

def multiplicar (*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar (1,2,3,4,5)
print (multiplicacao)

# Resultado: 120

'''
Exercícios com Funcões

Crie uma funcao que fale se um número é par ou ímpar.
Retorne se o número é par ou ímpar.

'''

# Sem o if.
def par_impar(numero):
    return numero % 2 == 0

# Resultado: 
# True
# False
# False
# True


# Com o "if" e com o "else" redundante.
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    else:
        return f'{numero} é ímpar'


# 2 é par
# 3 é ímpar
# 15 é ímpar
# 16 é par

# Se o "else" redundante:
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print (par_impar(2))
print (par_impar(3))
print (par_impar(15))
print (par_impar(16))
'''
Introducao as funcoes (def) em Python
Funcoes sao trechos de código usados para 
replicar determinada acao ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funcoes Python retornam None (nada).

Funções podem usar parâmetros para receber valores. 
Parâmetro é o nome da "variável" dentro dos parênteses.
Argumento é o valor passado para o parâmetro no momento da execução da função.

'''

def funcao_print():
    print ('Várias1')
    print ('Várias2')

funcao_print()

# Várias1
# Várias2

def funcao_print(a, b, c):
    print (a)
    print (b)
    print(c)

funcao_print('silmara', 'parametro', 'argumentos')

# silmara
# parametro
# argumentos

def funcao_print(a, b, c):
    print (a, b, c)

funcao_print('silmara', 'parametro', 'argumentos')
# silmara parametro argumentos
funcao_print(4, 5, 6)
# 4 5 6


def saudacao(nome='Sem nome'):
    print (f'Olá, {nome}')

saudacao('Silmara')
saudacao('Eliza')
saudacao('Silva')
saudacao()

# Olá, Silmara
# Olá, Eliza
# Olá, Silva
# Olá, Sem nome

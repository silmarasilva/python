"""
Higher Order Functions
Funções de primeira classe
"""

# Funcao chamando Funcao, funcao como argumento de outras funcoes
def saudacao(msg):
    return msg

def executa_funcao(funcao, texto):
    return funcao(texto)

variavel = executa_funcao(saudacao, "Bom dia, texto qualquer passado como parâmetro da func saudacao(msg)")
print (variavel)



# Funcao chamando Funcao, funcao como argumento de outras funcoes

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)
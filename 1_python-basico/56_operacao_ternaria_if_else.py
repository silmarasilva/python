"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

# A operação ternária (também chamada de condicional de uma linha) é uma maneira compacta de escrever uma condição em Python, onde você pode escolher entre dois valores dependendo de uma condição. Ela segue a estrutura:

# <valor se verdadeiro> if <condição> else <valor se falso>

# Como funciona?
# A estrutura básica é uma expressão condicional, que avalia a <condição>. Se a condição for verdadeira (True), o valor antes do if é escolhido. Se a condição for falsa (False), o valor depois do else é escolhido.

condicao = 10 == 11  # Condição falsa
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)  # Vai imprimir 'Outro valor'


idade = 18
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)


# Se o saldo for maior que 500, aplicamos um desconto de 10% (saldo * desconto). Caso contrário, mantemos o valor do saldo sem alterações.

saldo = 1000
desconto = 0.1
valor_com_desconto = saldo - (saldo * desconto) if saldo > 500 else saldo
print(valor_com_desconto) # 900.0

# Decisão de status em um sistema:
# Você pode usar a operação ternária para tomar decisões rápidas em sistemas que retornam status, como verificar se um usuário tem permissão para acessar determinado recurso.

usuario_logado = True
acesso = "Permitido" if usuario_logado else "Negado"
print(acesso)


# Outras formas de usar
# Você pode usar a operação ternária em situações mais complexas e aninhadas.

digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)  # Vai imprimir 9

# Em um contexto de funções:
# Você pode também usar a operação ternária em funções, para retornar um valor rapidamente dependendo de uma condição.

def validar_idade(idade):
    return "Maior de idade" if idade >= 18 else "Menor de idade"

print(validar_idade(20))  # Saída: Maior de idade
print(validar_idade(15))  # Saída: Menor de idade


# Mudando valores em uma condição (invertido)


digito = 12
novo_digito = 0 if digito > 9 else digito
print(novo_digito)  # Vai imprimir 0

# Operação ternária aninhada
# Você também pode aninhar múltiplas condições ternárias para criar escolhas mais complexas, porém não é recomendado.

print('Valor' if False else 'Outro valor' if False else 'Fim')


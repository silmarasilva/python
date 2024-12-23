# A avaliação de curto-circuito (short-circuit evaluation) é um comportamento dos operadores lógicos em Python (and e or) onde a avaliação das expressões é interrompida assim que o resultado final é determinado. Isso significa que nem todas as partes da expressão precisam ser avaliadas.


# Em Python, o valor de uma variável é considerado "falsy" (ou seja, avaliado como False em um contexto booleano) se ele for um dos seguintes:

# 0 (zero) para números (inteiros, floats, etc.)
# Sequências ou coleções vazias (como listas, strings, dicionários, etc.)
# O valor especial None
# O valor literal False

# Como funciona a avaliação de curto-circuito

# 1. Operador and
# O operador and retorna o primeiro valor "falsy" encontrado.
# Se não houver valores "falsy", ele retorna o último valor avaliado.

x = 0
y = 1
z = 2

resultado = x and y and z  # Avaliação de curto-circuito interrompe em `x`
print(resultado)  # Saída: 0 (primeiro valor "falsy")

# 2. Operador or
# O operador or retorna o primeiro valor "truthy" encontrado.
# Se todos os valores forem "falsy", ele retorna o último valor avaliado.

a = 0
b = False
c = 2

resultado = a or b or c  # Avaliação de curto-circuito interrompe em `c`
print(resultado)  # Saída: 2 (primeiro valor "truthy")


# Por que a avaliação de curto-circuito é útil?

# Eficiência:
# Evita a execução de partes desnecessárias de uma expressão lógica.
# Exemplo:

x = 0
resultado = x and expensive_function()  # `expensive_function` nunca é chamada


# Imagine que você está desenvolvendo um sistema que processa uma ação apenas se uma condição inicial for verdadeira. Essa condição inicial é representada por x. Caso contrário, o sistema deve ignorar o restante da operação porque ela seria desnecessária e cara em termos de processamento.StopAsyncIteration
    
# No código:
# x representa uma condição inicial que determina se vale a pena executar a função.
# expensive_function() representa uma operação complexa que só deve ser chamada se x for "truthy".

# Imagine um sistema que gera relatórios financeiros. Antes de fazer cálculos detalhados (uma operação cara), verificamos se o relatório está habilitado (x = 1 ou x = 0).

x = 0
resultado = x and expensive_function()  # `expensive_function` nunca é chamada

def expensive_function():
    print("Função custosa chamada!")
    return "Resultado do relatório"

# Cenário 1: Relatório está desabilitado
x = 0  # "Relatório desabilitado"
resultado = x and expensive_function()
print(resultado)  # Saída: 0
# A função `expensive_function` nunca será chamada porque `x` é falsy.

# Cenário 2: Relatório está habilitado
x = 1  # "Relatório habilitado"
resultado = x and expensive_function()
print(resultado)  # Saída: "Resultado do relatório"
# Agora `expensive_function` será chamada porque `x` é truthy.



# Evitar Erros:
# Pode ser usada para evitar erros ao verificar condições que dependem de outras.
# Exemplo:

lista = []
if lista and lista[0] == 10:  # `lista[0]` nunca será avaliado se `lista` for vazia
    print("Primeiro elemento é 10")


# Outro Exemplo Prático: Checagem de Erros
# Antes de acessar o primeiro elemento de uma lista, verificamos se ela não está vazia:

lista = []

# Só tenta acessar o primeiro elemento se a lista não estiver vazia
resultado = lista and lista[0]
print(resultado)  # Saída: []

lista = [10, 20, 30]
resultado = lista and lista[0]
print(resultado)  # Saída: 10



# Substituir if simples:
# Em alguns casos, a lógica de curto-circuito pode ser usada para simplificar o código.
# Exemplo:
nome = input("Digite seu nome: ") or "Anônimo"  # Define um valor padrão
print(nome)

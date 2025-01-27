"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

"""

def soma (x, y):
    print (x, y)

soma(1, 2)

# 1 2

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3) # x=1 y=2 z=3 | x + y + z =  6
soma(1, y=2, z=5) # x=1 y=2 z=5 | x + y + z =  8
print(1, 2, 3, sep='-') # 1-2-3

# Quando falamos em argumentos, estamos falando sobre os valores passados para as funções no ato da sua execução. Existem argumentos nomeados e argumentos posicionais.

# Argumentos nomeados recebem o nome do parâmetro antes do valor, argumentos posicionais recebem apenas o valor para preencher o parâmetro na ordem.

# Por qual motivo você usaria argumentos nomeados? É interessante usar argumentos nomeados ppara poderar alterar a ordem no envio de valores para a funcao.

# Você não pode enviar argumento pposicionais após argumentos nomeados.
"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

# É possível enviar valores padrão para parâmetros de função. Esse valor é inserido na definicao da funcao.
# def soma(x, y, z=None):


def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2) # x=1 y=2 3
soma(3, 5) # x=3 y=5 8
soma(100, 200) # x=100 y=200 300
soma(7, 9, 0) # x=7 y=9 z=0 16
soma(y=9, z=0, x=7) # x=7 y=9 z=0 16
# Problema: Gere a tabuada de um número fornecido.

def multiplication_table(number):
    return [f"{number} x {i} = {number * i}" for i in range(1, 11)]

print("\n".join(multiplication_table(5)))

# 5 x 1 = 5
# ...
# 5 x 10 = 50

#O método join() une todos os itens da lista (que são strings) em uma única string, separando-os por "\n", ou seja, cada item será impresso em uma linha diferente.
"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)


# 1
# 11 2
# 11
# 11

"""
A palavra-chave global faz com que as alterações feitas em x dentro das funções 
se apliquem à variável global definida fora delas.
O valor de x global é alterado progressivamente:
Inicia como 1.
É alterado para 10 na função escopo.
É alterado para 11 na função outra_funcao.
A variável y é local à função outra_funcao e não afeta nada fora dela.

"""
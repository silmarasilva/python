"""

A call stack em Python é uma estrutura de dados utilizada para gerenciar a execução de funções em um programa. Ele funciona como uma pilha (stack), onde cada chamada de função adiciona (ou "empilha") um novo "frame" no topo da pilha, e a execução da função atual é pausada enquanto a nova função é executada. Quando a função chamada é concluída, seu "frame" é removido (ou "desempilhado") e a execução retorna para o ponto onde a função foi chamada.

Como funciona o call stack?

1. Chamada de função: Quando uma função é chamada, Python cria um "frame" de execução contendo informações como:

2. Valores dos argumentos passados.
Variáveis locais da função.
O ponto no código para onde retornar após a execução.
Execução da função: O frame da função chamada é adicionado ao topo do call stack, e Python pausa a execução da função anterior até que a função atual seja concluída.

3. Retorno da função: Quando a função termina sua execução (ou retorna um valor), seu frame é removido do topo do stack, e a execução continua de onde parou na função anterio

"""
def func1():
    print("Start func1")
    func2()
    print("End func1")

def func2():
    print("Start func2")
    func3()
    print("End func2")

def func3():
    print("Inside func3")

func1()

# Start func1
# Start func2
# Inside func3
# End func2
# End func1

"""
Importância do Call Stack
Controle de Fluxo: Ele gerencia a sequência de chamadas de funções e retorna à função correta após a execução.
Tratamento de Erros: Em casos de exceções, Python fornece o "traceback" com base no estado do call stack, mostrando as funções que estavam em execução no momento do erro.
Recursão: Em chamadas recursivas, o call stack armazena cada chamada da função, podendo levar a um "Stack Overflow" se o limite de recursão for excedido.
"""
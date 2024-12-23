"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 5
linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
print('Acabou')


# Exemplo Prático: Imprimindo uma Tabela de Multiplicação

qtd_linhas = 10  # Define o número de linhas (até 10)
qtd_colunas = 10  # Define o número de colunas (até 10)
linha = 1

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha} x {coluna} = {linha * coluna}', end='\t')  # Imprime na mesma linha com tabulação
        coluna += 1
    print()  # Quebra a linha ao fim de cada linha da tabela
    linha += 1

print('Tabela de Multiplicação Finalizada!')

# Como funciona o código acima?
# Variáveis:
# qtd_linhas e qtd_colunas definem os limites da tabela.
# linha e coluna são usadas como índices para navegar pela tabela.
# Laço externo (while linha <= qtd_linhas):
# Representa cada linha da tabela.
# Laço interno (while coluna <= qtd_colunas):
# Representa cada coluna dentro da linha.
# Exibição:
# O comando end='\t' adiciona uma tabulação ao final da impressão, deixando os valores alinhados.
# O comando print() vazio quebra a linha ao final de cada linha da tabela.


# 1 x 1 = 1    1 x 2 = 2    1 x 3 = 3    ...    1 x 10 = 10
# 2 x 1 = 2    2 x 2 = 4    2 x 3 = 6    ...    2 x 10 = 20
# 3 x 1 = 3    3 x 2 = 6    3 x 3 = 9    ...    3 x 10 = 30
# ...
# 10 x 1 = 10  10 x 2 = 20  10 x 3 = 30  ...    10 x 10 = 100
# Tabela de Multiplicação Finalizada!



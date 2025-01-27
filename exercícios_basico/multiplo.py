# Problema: Verifique se um número é múltiplo de outro.


def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)

# 16 é múltiplo de 8? True
# 15 é múltiplo de 3? True
# 10 é múltiplo de 2? True

"""
A função recebe dois argumentos: numero e multiplo.
Ela verifica se o número (numero) é divisível pelo possível múltiplo (multiplo) sem deixar resto.
Isso é feito usando o operador de módulo (%), que retorna o resto da divisão.
Se o resto da divisão for zero (numero % multiplo == 0), então numero é múltiplo de multiplo.

Quando você usa end=' ', está dizendo ao Python para substituir a quebra de linha padrão por um espaço em branco ou qualquer outro texto especificado. Assim, a próxima impressão continuará na mesma linha, logo após o espaço.

O código está imprimindo True ou False porque a variável resultado na função multiplo_de armazena o valor lógico (bool) do cálculo da expressão numero % multiplo == 0.

A variável resultado é avaliada como um bool (valor lógico) porque a expressão atribuída a ela, numero % multiplo == 0, é uma comparação lógica. No Python, operadores de comparação como == sempre retornam um valor booleano: True ou False.

"""
# Problema: Valide se um CPF fornecido é válido ou não.

import re

def validate_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
        return False
    for i in range(9, 11):
        value = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digit = (value * 10 % 11) % 10
        if digit != int(cpf[i]):
            return False
    return True

print(validate_cpf("746.824.890-70"))  # True
print(validate_cpf("123.456.789-00"))  # False

"""
O CPF é composto por 11 dígitos numéricos, 
e a validade do CPF é verificada com base em dois últimos dígitos de controle, 
que são calculados a partir dos 9 primeiros dígitos.

A função re.sub(r'\D', '', cpf) utiliza a expressão regular \D, 
que corresponde a qualquer caractere não numérico (diferente de 0-9).

Essa linha remove pontos, traços e outros caracteres 
não numéricos de uma string de CPF. Por exemplo, 
746.824.890-70 vira 74682489070.

A primeira parte da verificação, len(cpf) != 11, 
checa se o CPF tem exatamente 11 dígitos.

A segunda parte, cpf == cpf[0] * len(cpf), 
verifica se todos os 11 dígitos são iguais.

Isso é importante porque CPFs como 111.111.111-11 ou 222.222.222-22 
são inválidos por serem números repetidos, sem valor real.

No FOR é realizada a validação dos dois últimos dígitos do CPF, 
que são chamados de dígitos verificadores. 
O cálculo de cada um desses dígitos segue um processo semelhante:

O loop percorre os índices 9 e 10 
(correspondentes aos dois últimos dígitos do CPF).
Em cada iteração, o cálculo do valor leva em consideração 
os 9 primeiros dígitos do CPF e um peso específico para cada posição:

Para o primeiro dígito verificador (posição 9), 
o peso é de 10 para o primeiro dígito do CPF, 9 
para o segundo, até 2 para o nono.
Para o segundo dígito verificador (posição 10), 
o peso vai de 11 para o primeiro dígito do CPF até 2 para o nono.

O cálculo do dígito verificador é feito com a fórmula:
digit = (value * 10 % 11) % 10

Aqui, primeiro multiplicamos value por 10 e aplicamos o módulo 11. 
Depois, aplicamos o módulo 10 para garantir que o dígito seja um número de 0 a 9.

Se o dígito calculado não for igual ao dígito do CPF fornecido, retornamos False
    
Se todas as verificações passarem, a função retorna True, indicando que o CPF é válido.

"""
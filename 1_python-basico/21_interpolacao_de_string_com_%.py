# Interpolação de strings em Python utilizando a sintaxe de placeholders (%) permite formatar valores dentro de strings de maneira precisa.

"""
Placeholders e Tipos de Dados
Os placeholders são marcadores dentro de strings que indicam o tipo de valor que será inserido. Os mais usados são:

%s: Insere uma string (str).
%d ou %i: Insere um número inteiro (int).
%f: Insere um número decimal (float).
%x ou %X: Insere um número no formato hexadecimal (letras minúsculas em %x, maiúsculas em %X).
"""

#Interpolacao de String
nome = 'Silmara'
preco = 100.95897643
variavel = '%s, o preco total foi R$%f' % (nome, preco)
print(variavel)

# Reduzindo casas decimais no R$
nome = 'Silmara'
preco = 100.95897643
variavel = '%s, o preco total foi R$%.2f' % (nome, preco)
print(variavel)


print('O hexadecimal de %d é %x' % (15, 15))    # O hexadecimal de 15 é f
print('O hexadecimal de %d é %04x' % (15, 15))  # O hexadecimal de 15 é 000f
print('O hexadecimal de %d é %04X' % (15, 15))  # O hexadecimal de 15 é 000F
print('O hexadecimal de %d é %08X' % (15, 15))  # O hexadecimal de 15 é 0000000F 


# Exemplo: Logs de Sistema
# Em aplicações reais, mensagens de log frequentemente usam esse tipo de interpolação para formatar informações dinâmicas.

import logging

# Configurando o nível de log
logging.basicConfig(level=logging.INFO)

# Interpolação para mensagens de log
usuario = "Silmara"
acao = "login"
status = "sucesso"

# Log formatado com %s
logging.info("Usuário: %s realizou a ação: %s com status: %s", usuario, acao, status)

# Saída no console:
# INFO:root:Usuário: Silmara realizou a ação: login com status: sucesso






# O hexadecimal é um sistema de numeração que utiliza a base 16 para representar valores. É muito usado em programação e computação porque se relaciona diretamente com a base 2 (binária), o sistema que os computadores utilizam.

# Como Funciona o Sistema Hexadecimal?
# Base 16:

# Ele possui 16 símbolos diferentes:
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
# Os números de 0 a 9 são iguais aos do sistema decimal.
# As letras de A a F representam os valores de 10 a 15.
# Exemplo:

# Decimal: 15
# Hexadecimal: F
# Decimal: 255
# Hexadecimal: FF

# Conversão para Binário
# O hexadecimal é útil porque cada dígito hexadecimal corresponde exatamente a 4 bits no sistema binário. Isso facilita a leitura de valores binários longos.

# Exemplo:
# Hexadecimal: F
# Binário: 1111
# Hexadecimal: 2A
# Binário: 0010 1010
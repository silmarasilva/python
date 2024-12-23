# Fatiamento de Strings em Python
# Fatiamento é uma técnica que permite acessar partes específicas de uma string, utilizando índices. Em Python, as strings podem ser acessadas por meio de índices positivos (da esquerda para a direita) ou negativos (da direita para a esquerda).

# Exemplo de índices:
# String: Olá mundo
# Índices positivos: 0 1 2 3 4 5 6 7 8
# Índices negativos: -9 -8 -7 -6 -5 -4 -3 -2 -1

# Sintaxe do fatiamento:
# string[início:fim:passo]

# início: índice onde o fatiamento começa (inclusivo).
# fim: índice onde o fatiamento termina (exclusivo).
# passo: intervalo entre os índices selecionados.
# Observação: A função len retorna a quantidade de caracteres da string. Isso pode ser útil para determinar os índices.

# Inverter a string utilizando índice negativo
variavel = 'Olá mundo'
print(variavel[::-1])  
# Saída: 'odnum álO'
# O passo negativo (-1) faz o fatiamento percorrer a string de trás para frente.

# Exibir toda a string com fatiamento completo
variavel = 'Olá mundo'
print(variavel[0:9])  
# Saída: 'Olá mundo'
# O índice inicial é 0 e o final é 9 (exclusivo), abrangendo todos os caracteres da string.

# Fatiamento padrão (sem parâmetros explícitos)
variavel = 'Olá mundo'
print(variavel[::])  
# Saída: 'Olá mundo'
# Sem parâmetros, o padrão é início=0, fim=len(variavel), passo=1.

# Utilizando len() para medir o tamanho de pedaços da string
variavel = 'Olá mundo'
print(len(variavel[3]))  
# Saída: 1
# `variavel[3]` retorna apenas o caractere no índice 3 (' '), que tem comprimento 1.

variavel = 'Olá mundo'
print(len(variavel[3:5]))  
# Saída: 2
# `variavel[3:5]` retorna os caracteres dos índices 3 e 4 (' m'), que têm comprimento total de 2.

# Exibir caracteres alternados (passo=2)
print(variavel[0:9:2])  
# Saída: 'Oámno'
# O passo de 2 pega um caractere a cada dois, começando no índice 0.


### Notas Adicionais
# - Se o índice **início** for omitido, o fatiamento começa no início da string (índice 0).
# - Se o índice **fim** for omitido, o fatiamento vai até o final da string.
# - Se o índice **passo** for negativo, o fatiamento será feito de trás para frente.


# Fatiamento omitindo índices
print(variavel[:5])  
# Saída: 'Olá m'
# Do início até o índice 5 (não inclui o 5).

print(variavel[4:])  
# Saída: 'mundo'
# Do índice 4 até o final.

print(variavel[-5:-1])  
# Saída: 'mund'
# Do índice -5 (inclusivo) até -1 (exclusivo).



"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
o índice final
"""
variavel = 'Olá mundo'
print(variavel[::-1])       # odnum álO  -> índice negativo inverte a string
print(variavel[0:9])        # Olá mundo
print(variavel[::])         # Olá mundo
print(len(variavel[3]))     # 1
print(len(variavel[3:5]))   # 2
print(variavel[0:9:2])      # Oámno




# Exemplo prático 1: Extração de partes de uma data
# Imagine que você recebe uma string representando uma data no formato "YYYY-MM-DD" (ano-mês-dia) e precisa extrair separadamente o ano, o mês e o dia.



# Extrair o ano
data = "2024-12-07"
ano = data[:4]
# Os primeiros 4 caracteres correspondem ao ano
print("Ano:", ano)  
# Saída: Ano: 2024

# Extrair o mês
data = "2024-12-07"
mes = data[5:7]
# Os caracteres no índice 5 e 6 correspondem ao mês
print("Mês:", mes)  
# Saída: Mês: 12

# Extrair o dia
data = "2024-12-07"
dia = data[8:]
# Do índice 8 até o final corresponde ao dia
print("Dia:", dia)  
# Saída: Dia: 07


# Exemplo prático 2: Máscara de CPF
# Outro caso muito comum é a manipulação de números de documentos, como um CPF. Imagine que você tem um CPF sem formatação (12345678909) e deseja formatá-lo como 123.456.789-09.

cpf = "12345678909"

# Adicionar a máscara ao CPF utilizando fatiamento
cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
# - Os primeiros 3 caracteres (cpf[:3]) correspondem ao primeiro bloco.
# - Os caracteres de índice 3 a 5 (cpf[3:6]) correspondem ao segundo bloco.
# - Os caracteres de índice 6 a 8 (cpf[6:9]) correspondem ao terceiro bloco.
# - Do índice 9 em diante (cpf[9:]) é o sufixo.

print("CPF formatado:", cpf_formatado)
# Saída: CPF formatado: 123.456.789-09

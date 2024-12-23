"""
Referência:
https://docs.python.org/pt-br/3/library/stdtypes.html

Tipos imutáveis que vimos: str, int, float, bool
"""

# Exemplo de manipulação de string (str):
string = 'Silmara Eliza'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print("String original:", string)  # Imprime a string original
print("String modificada:", outra_variavel)  # Imprime a string com modificação

# Métodos de string:

# Método capitalize: Coloca a primeira letra em maiúsculo e o restante em minúsculo
string = 'Silmara Eliza'
print("Método capitalize:", string.capitalize())  # Saída: Silmara eliza

# Método lower: Converte toda a string para letras minúsculas
print("Método lower:", string.lower())  # Saída: silmara eliza

# Método zfill: Preenche a string com zeros à esquerda até atingir o comprimento especificado
string = '1'
print("Método zfill:", string.zfill(10))  # Saída: 0000000001





# Exemplo: Formatar e validar dados de um formulário de cadastro

# Nome completo do usuário
nome_usuario = "silmara eliza"

# UPPER: A list comprehension [palavra.upper() for palavra in nome_usuario.split()] aplica o método upper em cada palavra.
# SPLIT: divide a string em uma lista de palavras com base nos espaços (['silmara', 'eliza']).
# STRIP: remove os espaços extras no início e no final da string.
# JOIN: combina as palavras de volta em uma string única, separando-as por espaços.

nome_formatado = " ".join([palavra.upper() for palavra in nome_usuario.strip().split()])
print("Nome formatado:", nome_formatado) # Saída: SILMARA ELIZA

# E-mail do usuário (entrada do formulário)
email_usuario = "SILMARA.ELIZA@EXEMPLO.COM"

# Converter o e-mail para letras minúsculas (evitar problemas de case sensitivity)
email_formatado = email_usuario.lower()
print("E-mail formatado:", email_formatado)  # Saída: silmara.eliza@exemplo.com

# ID de cadastro do usuário
id_usuario = "123"

# Garantir que o ID tenha sempre 10 dígitos, preenchendo com zeros à esquerda
id_formatado = id_usuario.zfill(10)
print("ID formatado:", id_formatado)  # Saída: 0000000123


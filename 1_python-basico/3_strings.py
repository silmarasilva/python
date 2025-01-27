# Python: Linguagem de programação
# Tipo de tipagem: Dinâmica (detecta automaticamente o tipo de dado) e Forte (não permite operações inválidas entre tipos diferentes, como somar um número com uma string).

# Strings (str): São textos delimitados por aspas.

# Exemplo 1: Uso de aspas simples
print('Silmara Irons')  # Saída: Silmara Irons

# Exemplo 2: Uso de aspas duplas
print("Silmara Irons")  # Saída: Silmara Irons

# Exemplo 3: Uso do caractere de escape (\)
# O caractere de escape (\) indica que o próximo caractere deve ser interpretado de forma especial.
# Aqui, \" permite incluir aspas duplas dentro de uma string delimitada por aspas duplas.
print("Silmara \"Irons\"")  # Saída: Silmara "Irons"

# Exemplo 4: String raw (r antes da string)
# Adicionando um 'r' antes das aspas, o Python trata a string como "raw" (bruta), 
# ignorando o efeito do caractere de escape.
print(r"Silmara \"Irons\"")  # Saída: Silmara \"Irons\"

# Exemplo 5: Misturando tipos na função print
# A função print pode receber múltiplos argumentos separados por vírgulas.
# Aqui, imprimimos um número inteiro e uma string.
print(1, 'Silmara "Irons"')  # Saída: 1 Silmara "Irons"

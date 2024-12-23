"""
split e join com list e str

- **split**: Divide uma string em uma lista, utilizando o separador especificado (padrão é espaço).
- **join**: Une uma lista de strings em uma única string, utilizando um separador especificado.

Funções auxiliares para manipulação de espaços em strings:
- **lstrip**: Remove espaços em branco à esquerda da string.
- **rstrip**: Remove espaços em branco à direita da string.
- **strip**: Remove espaços em branco do início e do fim da string.
"""

frase = '   Olha só que   , coisa interessante          '  # String com espaços indesejados
lista_frases_cruas = frase.split(',')  # Divide a string usando ',' como separador
lista_frases = [frase.strip() for frase in lista_frases_cruas]  # Remove espaços extras de cada item da lista
print("Lista com espaços indesejados:", lista_frases_cruas)  # # ['   Olha só que   ', ' coisa interessante          ']
print("Lista tratada:", lista_frases)  # # ['Olha só que', 'coisa interessante']
frases_unidas = ', '.join(lista_frases)  # Une os elementos da lista em uma única string
print("Frases unidas:", frases_unidas)  # # Olha só que, coisa interessante


frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',') # split separa palavras

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) # strip remove espacos

print(lista_frases_cruas)
print(lista_frases)

frases_unidas = ', '.join(lista_frases) # join, junta
print(frases_unidas)

frase = 'O Python é uma linguagem de programacão multiparadigma. Python foi criado por guido van Rossum.'
print (frase.count('Python'))


# O loop percorre cada letra da string.
# Para cada letra, ele conta quantas vezes ela aparece na string.
# Se a frequência da letra for maior do que a frequência máxima encontrada até agora, ele atualiza os valores.
# Ao final, ele imprime a letra mais frequente e sua quantidade de ocorrências.

frase = 'aaabbbcccc'
indice_atual = 0
frequencia_maxima = 0
letra_mais_frequente = ''

while indice_atual < len(frase):
    letra_atual = frase[indice_atual]

    if letra_atual == ' ':  # Ignorar espaços
        indice_atual += 1
        continue

    frequencia_letra_atual = frase.count(letra_atual) # função count é usada para contar quantas vezes a letra atual aparece na string (frase).

    if frequencia_maxima < frequencia_letra_atual:  
        frequencia_maxima = frequencia_letra_atual
        letra_mais_frequente = letra_atual

    indice_atual += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_frequente}". Ela apareceu '
    f'{frequencia_maxima}x'
)

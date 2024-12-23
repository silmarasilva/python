"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

# Exemplo 1: Ignorar valores específicos e interromper o loop

contador = 0
while contador <= 99:
    contador += 1
    
    # Ignora o número 6
    if contador == 0:
        print('Não vou mostrar o 6.')
        continue
    
    # Imprime os outros valores
    print(contador)

print('Acabou')


# Exemplo 2: Simples, ignorando apenas um número

contador = 0
while contador <= 100:
    contador += 1

    # Ignora o número 6
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    # Imprime os outros valores
    print(contador)

    # Interrompe o loop no número 40
    if contador == 40:
        break

print('Acabou')

# Exemplo 3: Ignorar um intervalo de valores

contador = 0
while contador <= 100:
    contador += 1

    # Ignora os números entre 10 e 27
    if 10 <= contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    # Imprime os outros valores
    print(contador)

    # Interrompe o loop no número 40
    if contador == 40:
        break

print('Acabou')


# Pontos importantes
# continue: Utilizado para pular uma iteração do loop.
# break: Finaliza o loop imediatamente.
# A organização do código ajuda a evitar confusões, especialmente quando há várias condições.
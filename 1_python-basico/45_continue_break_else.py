# Loop principal de 0 a 9 - COTINUE, BREAK, ELSE, ETC.

for i in range(10):
    # Verifica se i é igual a 2 e pula para a próxima iteração
    if i == 2:
        print('i é 2, pulando...')
        continue  # Ignora o restante do código abaixo no loop atual

    # Verifica se i é igual a 8 e interrompe o loop
    if i == 8:
        print('i é 8, seu else não executará')
        break  # Sai do loop principal

    # Loop interno de 1 a 2 (número de repetições fixo)
    for j in range(1, 3):
        print(i, j)  # Imprime o valor atual de i e j no loop interno

# Else associado ao loop principal: executa apenas se o loop NÃO for interrompido por um `break`
else:
    print('For completo com sucesso!')


# Loop interno com range(1, 3):
# Para cada valor de i, executa duas vezes, imprimindo os pares (i, j).

# Como funciona range(1, 3)
# range(start, stop) gera números começando em start (inclusive) até stop (exclusive).
# Neste caso, range(1, 3) gera a sequência [1, 2]. 
# Isso significa que o loop será executado duas vezes com j assumindo os valores:
# Primeira iteração: j = 1
# Segunda iteração: j = 2
# Para cada valor de i no loop externo, 
# o loop interno será executado exatamente 2 vezes (porque range(1, 3) tem 2 elementos).


# i = 0, j = 1
# i = 0, j = 2
# i = 1, j = 1
# i = 1, j = 2
# i = 2, j = 1
# i = 2, j = 2

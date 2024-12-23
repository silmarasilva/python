""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')


# O while/else é utilizado em cenários onde você deseja executar um bloco de código adicional se o laço while não for interrompido por um break. 
# Um exemplo prático disso é verificar um item em uma lista e realizar uma ação caso o item não seja encontrado.

# Lista de números
numeros = [10, 20, 30, 40, 50]

# Número que queremos encontrar
procurado = 25

i = 0
while i < len(numeros):
    numero_atual = numeros[i]

    # Se encontrar o número, interrompe o loop
    if numero_atual == procurado:
        print(f'Número {procurado} encontrado na posição {i}.')
        break

    i += 1
else:
    # Executa se o break não foi chamado no loop
    print(f'Número {procurado} não encontrado na lista.')

print('Fim da execução.')

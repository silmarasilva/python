"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Insira um número inteiro: ')
if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):
    numero = int(entrada) # converte a entrada em inteiro.
    if numero % 2 == 0: # verifica se é par.
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar.')
else: 
    print ('A entrada não é um número inteiro.')


#O método .isdigit() verifica se todos os caracteres na string são números (positivo).
# (entrada[0] == '-' and entrada[1:].isdigit()). Isso verifica se o primeiro caractere é um - e os outros caracteres são dígitos.


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# Solicita que o usuário insira a hora
entrada = input("Que horas são agora (0-23)? ")

# Verifica se a entrada é um número inteiro válido para horas
if entrada.isdigit():
    hora = int(entrada)
    if 0 <= hora <= 23:  # Verifica se a hora está no intervalo válido
        if 0 <= hora <= 11:
            print("Bom dia!")
        elif 12 <= hora <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")
    else:
        print("Por favor, insira uma hora válida entre 0 e 23.")
else:
    print("Entrada inválida. Por favor, insira um número inteiro.")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Solicita o primeiro nome do usuário
nome = input("Digite seu primeiro nome: ")

# Verifica o comprimento do nome
tamanho_nome = len(nome)

# Determina a classificação do nome com base no tamanho
if tamanho_nome <= 4:
    print("Seu nome é curto.")
elif 5 <= tamanho_nome <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")
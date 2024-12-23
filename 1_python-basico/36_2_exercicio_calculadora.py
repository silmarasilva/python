""" Calculadora com while """
while True:
    numero_1= input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+, -, /, *): ')


    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)

    except ValueError:
        print ('Um ou ambos os números digitados são inválido')
        numeros_validos = None
        continue

    # Verificação de operadores válidos
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos or len(operador) != 1:
        print ('Operador inválido. Use apenas um dos seguintes: +, -, /, *')
        continue

    # Evitar divisão por zero
    if operador == '/' and num_2_float == 0:
        print('Erro: Divisão por zero não é permitida.')
        continue

    # Determinar se os números podem ser exibidos como inteiros
    # Verifica se o número pode ser convertido em um inteiro sem perda de precisão usando numero.is_integer().Se for possível, exibe como um número inteiro; caso contrário, mantém o formato decimal
    def formatar_numero(numero):
        return int(numero) if numero.is_integer() else numero

    num_1 = formatar_numero(num_1_float)
    num_2 = formatar_numero(num_2_float)

    # Realizando a operação
    print('Realizando a sua conta, confira o resultado abaixo:')
    if operador == '+':
        resultado = num_1_float + num_2_float
        print(f'{num_1} + {num_2} = {resultado}')
    elif operador == '-':
        resultado = num_1_float - num_2_float
        print(f'{num_1} - {num_2} = {resultado}')
    elif operador == '/':
        resultado = num_1_float / num_2_float
        print(f'{num_1} / {num_2} = {resultado}')
    elif operador == '*':
        resultado = num_1_float * num_2_float
        print(f'{num_1} * {num_2} = {resultado}')


    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        print ('Calculadora encerrada.')
        break

    # startswith = comeca com a letra indicada

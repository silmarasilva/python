# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 string vazia '' e False
# Também existe o tipo None que é
# usado para representar um não valor

# Exemplo de uso do AND
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrada permitida')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)

# O que será exibido na saída (tela)?
if 0 and 1:
    print(True and 1)

# O 0 (zero) de 0 and 1 avalia como falsy. O corpo do if não será executado.


# O que será exibido na saída (tela)?
if 1 and 1:
    print(True and 1 and False)

# Passo 1: Avaliar if 1 and 1: Ambos os valores 1 são considerados truthy (verdadeiros).
# O if avalia como True, então o bloco dentro do if será executado.

# Passo 2: Avaliar True and 1 and False
# Aqui, o operador and avalia os operandos:

# True and 1: Ambos são "truthy". O operador and continua avaliando os próximos operandos e retorna o próximo valor.
# Resultado intermediário: 1.

# 1 and False:O valor 1 é "truthy", então o operador and continua avaliando e retorna o próximo valor.
# O próximo valor é False, que é "falsy".Resultado final: False.
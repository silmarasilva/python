# if / elif      / else
# se / se não se / se não

#-------exemplo 1--------------#

entrada = input('Você quer "entrar" ou "sair"? ')
nome_sistema = 'Vamonos Pest'

if entrada == 'entrar':
    print('Você entrou no sistema')
    print(f'Seja bem vindo, agora você está logado no "{nome_sistema}"') 

elif entrada == 'sair':
    print('Você saiu do sistema')

else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')

#-------exemplo 2--------------#


condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')


#------Sistema de Status de Pedidos------#

pedido_processado = False
pedido_enviado = False
pedido_entregue = True
pedido_atrasado = False

if pedido_processado:
    print('O pedido foi processado.')
    print('Agora ele está pronto para ser enviado.')
elif pedido_enviado:
    print('O pedido foi enviado.')
    print('Você receberá em breve.')
elif pedido_entregue:
    print('O pedido já foi entregue.')
    print('Agradecemos por comprar conosco!')
elif pedido_atrasado:
    print('O pedido está atrasado.')
    print('Pedimos desculpas pelo transtorno. Estamos verificando.')
else:
    print('O pedido ainda não foi processado.')

# Outra verificação independente
if 10 == 10:
    print('Sempre verdadeiro. Isso pode ser usado para ações específicas.')

print('Obrigado por usar nosso sistema.')



#-----Simulando dados do banco de dados-----#
pedido = {
    "id": 123,
    "status": "processado"  # Pode ser: processado, enviado, entregue, atrasado
}

# Verificação de status
if pedido["status"] == "processado":
    print('O pedido foi processado.')
elif pedido["status"] == "enviado":
    print('O pedido foi enviado.')
elif pedido["status"] == "entregue":
    print('O pedido foi entregue.')
elif pedido["status"] == "atrasado":
    print('O pedido está atrasado.')
else:
    print('Status do pedido desconhecido.')

print('Obrigado por usar nosso sistema.')


#-------Sistema login BankEasy--------------#

# Sistema de Controle de Acesso
entrada = input('Você quer "entrar", "sair" ou "suporte"? ')
nome_sistema = 'BankEasy'

if entrada.lower() == 'entrar':
    print('Você entrou no sistema.')
    print(f'Seja bem-vindo(a) ao {nome_sistema}!')
    # Simulação de login com dados de autenticação
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    if usuario == 'admin' and senha == '1234':
        print('Login realizado com sucesso!')
    else:
        print('Nome de usuário ou senha incorretos.')

elif entrada.lower() == 'sair':
    print('Você saiu do sistema.')
    print('Esperamos vê-lo novamente!')

elif entrada.lower() == 'suporte':
    print('Você acessou o suporte.')
    print('Nosso horário de atendimento é das 8h às 18h.')

else:
    print('Opção inválida. Tente novamente.')

print('Obrigado por usar o BankEasy.')
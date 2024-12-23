# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = 'Otávio'
print(nome[2])              #retorna á
print(nome[-4])             #retorna á    -> índice negativo conta de trás para frente.
print ('á' in nome)         #retorna True -> a letra á está contida na variável 'nome'
print('vio' in nome)        #retorna True -> 'vio' está contida na variável 'nome'
print('zero' in nome)       #retorna False 
print(10 * '-')             #retorna ---------- 
print('vio' not in nome)    #retorna False
print('zero' not in nome)   #retorna True


nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')


# Um cenário comum para usar os operadores in e not in é na validação de entradas do usuário. Por exemplo, ao verificar se um e-mail contém o símbolo @ e o domínio correto antes de prosseguir.

email = input("Digite seu e-mail: ")

# Verifica se o e-mail contém '@' e termina com '.com'
if '@' in email and email.endswith('.com'):
    print("E-mail válido! Continuando com o cadastro...")
else:
    print("E-mail inválido. Por favor, verifique e tente novamente.")



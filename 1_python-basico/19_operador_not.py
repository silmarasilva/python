# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')
if not senha:
    print ('Você não digitou nada')


print(not True)  # False
print(not False)  # True
print(not 1)      # false



# Um exemplo comum do operador lógico not no mundo real é o controle de login em sistemas. Vamos verificar se o usuário preencheu os campos obrigatórios, como nome de usuário e senha, antes de prosseguir.

# Validação de login simples
username = input("Digite seu nome de usuário: ")
password = input("Digite sua senha: ")

# Verifica se algum dos campos está vazio
if not username:
    print("Erro: O nome de usuário não pode estar vazio.")
elif not password:
    print("Erro: A senha não pode estar vazia.")
else:
    print(f"Bem-vindo, {username}!")

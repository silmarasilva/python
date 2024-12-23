"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
"""


# 1. Flag (Bandeira)
# Uma flag é como um marcador ou sinalizador no código.
# É usada para "lembrar" o estado de algo, indicando se uma condição foi atendida ou não.
# Exemplo:

# Você usa uma bandeira (flag) para verificar se uma operação foi realizada ou se uma condição foi cumprida.
# None
# Em Python, None representa ausência de valor ou que algo ainda não foi definido.
# Aqui, passou_no_if é inicializado como None para indicar que o bloco if ainda não foi executado.

passou_no_if = None  # Inicializa a flag com None, indicando que ainda não foi avaliado

# is e is not
# is verifica se duas variáveis referenciam o mesmo objeto na memória.
# is not verifica se elas referenciam objetos diferentes.

if passou_no_if is None:
    print('Não passou no if')  # Isso verifica se `passou_no_if` ainda é None.

# Essa linha confirma se a variável passou_no_if ainda está no estado inicial (não foi alterada pelo código).

condicao = False
passou_no_if = None  # Flag inicializada como None

if condicao:  # Verifica a condição
    passou_no_if = True  # Marca a flag como True se entrou no bloco `if`
    print('Faça algo')
else:
    print('Não faça algo')  # Executado porque `condicao` é False

# Verifica se a flag `passou_no_if` foi alterada
if passou_no_if is None:
    print('Não passou no if')  # Isso será impresso, porque `condicao` era False
else:
    print('Passou no if')

# Imagine um sistema onde você quer verificar se o usuário conseguiu fazer login.

# Inicializamos a flag para rastrear o status de login
usuario_logado = None  # Nenhum estado definido inicialmente

# Simulação de uma função que verifica as credenciais do usuário
def verificar_credenciais(usuario, senha):
    # Exemplo simples: credenciais corretas
    return usuario == "admin" and senha == "1234"

# Tentativa de login
usuario = "admin"
senha = "senha_errada"

# Verificação das credenciais
if verificar_credenciais(usuario, senha):
    usuario_logado = True  # Flag indicando sucesso no login
    print("Login bem-sucedido!")
else:
    usuario_logado = False  # Flag indicando falha no login
    print("Login falhou!")

# Verificação do estado de login
if usuario_logado is None:
    print("Nenhuma tentativa de login foi feita.")
elif usuario_logado is True:
    print("Usuário está logado.")
else:
    print("Usuário não está logado.")

# Estado Inicial: Usar None como estado inicial evita confusões e garante que o código saiba que nenhuma tentativa foi feita ainda.
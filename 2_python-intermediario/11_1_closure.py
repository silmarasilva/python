"""
Closure e funcoes que retornam outras funcoes.

Funções que retornam outras funções são chamadas de funções de ordem superior (Higher Order Functions). Elas podem retornar funções para serem usadas posteriormente. No exemplo a seguir, a função criar_saudacao cria uma função personalizada que pode ser chamada para gerar saudações específicas.

"""

def criar_saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'

saudacao_1 = criar_saudacao('Bom dia', 'Luiz')
print(saudacao_1)  # Output: Bom dia, Luiz

saudacao_2 = criar_saudacao('Boa noite', 'Luiz')
print(saudacao_2)  # Output: Boa noite, Luiz

"""
2. Closure
Uma closure ocorre quando uma função interna (função aninhada) "lembra" o ambiente em que foi criada, mesmo após o escopo externo ter terminado sua execução. Ou seja, a função interna pode acessar as variáveis da função externa. Isso permite que a função interna retenha o valor das variáveis de sua função externa, mesmo depois de a execução ter saído do escopo da função.
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar  # Retorna a função interna

# Criando as funções de saudação
saudacao_1 = criar_saudacao('Bom dia', 'Luiz')
saudacao_2 = criar_saudacao('Boa noite', 'Luiz')

# Chamando as funções retornadas
print(saudacao_1())  # Output: Bom dia, Luiz
print(saudacao_2())  # Output: Boa noite, Luiz

# Aqui, criar_saudacao retorna a função saudar, que "lembra" os valores de saudacao e nome mesmo após a execução da função criar_saudacao ter terminado.

"""
3. Funções de Ordem Superior com Parâmetros Variáveis
É possível criar closures ainda mais flexíveis, onde a função interna usa um parâmetro adicional. Neste exemplo, a função interna saudar usa o parâmetro nome para gerar a saudação para diferentes pessoas.
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar  # Retorna a função interna

# Criando as funções de saudação
saudacao_1 = criar_saudacao('Bom dia')
saudacao_2 = criar_saudacao('Boa noite')

# Usando a função gerada para diferentes nomes
for nome in ['Maria', 'Joao', 'Pedro', 'Luiza', 'Amanda']:
    print(saudacao_1(nome))  # Output: Bom dia, Maria, Joao, etc.
    print(saudacao_2(nome))  # Output: Boa noite, Maria, Joao, etc.

# Aqui, criar_saudacao cria funções de saudação que, quando chamadas, recebem um nome como argumento e geram a saudação apropriada.
# Manipulando chaves e valores em dicionários

pessoa = {}
chave = 'nome'

pessoa[chave] = 'Luiz Otávio' # add no dicionário "pessoa" um valor para a chave "nome"
pessoa['sobrenome'] = 'Miranda' # add no dicionário "pessoa" um valor para a chave "sobrenome"
print(pessoa[chave]) # Luiz Otávio
print(pessoa['sobrenome']) # Miranda
print(pessoa) # {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda'}

pessoa[chave] = 'Maria'
print(pessoa[chave]) # Maria
print(pessoa) # {'nome': 'Maria', 'sobrenome': 'Miranda'}

del pessoa['sobrenome']
print(pessoa) # {'nome': 'Maria'}
print(pessoa['nome']) # Maria

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE') # NÃO EXISTE
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')

"""

Chave dinâmica em dicionários
Uma chave dinâmica é uma maneira de acessar ou modificar um dicionário usando uma variável que contém o nome da chave, em vez de usar a chave diretamente como string. Isso é útil quando as chaves são determinadas em tempo de execução (durante a execução do código) e não são fixas no código-fonte.

A variável chave armazena a string 'nome'.
Quando você usa pessoa[chave], o Python substitui chave pelo valor armazenado nela (neste caso, 'nome').
Isso permite que você trabalhe com o dicionário de forma dinâmica, sem precisar codificar as chaves diretamente como strings.

Imagine que você está processando dados onde as chaves são determinadas de forma programática, como nomes de colunas de uma planilha ou campos de um formulário dinâmico.

dados = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
for chave in ['nome', 'idade', 'cidade']:
    print(f"{chave}: {dados[chave]}")

Aqui, as chaves são determinadas pelo loop, e não codificadas diretamente.


"""
# Adicionar valores dinamicamente:

pessoa = {}
for i in range(3):
    chave = f'chave_{i}'  # Gera nomes de chave dinamicamente
    pessoa[chave] = i * 10  # Adiciona valores ao dicionário
print(pessoa)  # {'chave_0': 0, 'chave_1': 10, 'chave_2': 20}


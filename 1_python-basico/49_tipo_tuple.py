"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)

# 1. Mutabilidade

# Em Python, listas e tuplas são estruturas de dados que permitem armazenar coleções de elementos. A principal diferença entre elas está na mutabilidade e em seus usos. Por esse motivo ela é um pouco mais eficiente. Aqui estão as diferenças principais:

# Lista: Mutável, ou seja, você pode modificar os elementos, adicionar, remover ou alterar itens.

lista = [1, 2, 3]
lista[0] = 10  # Altera o primeiro elemento
lista.append(4)  # Adiciona um elemento
print(lista)  # Saída: [10, 2, 3, 4]

# Tupla: Imutável, ou seja, uma vez criada, seus elementos não podem ser modificados.

tupla = (1, 2, 3)
# tupla[0] = 10  # Isso causaria um erro
print(tupla)  # Saída: (1, 2, 3)



# 2. Desempenho
# Lista: Como é mutável, tende a ser um pouco mais lenta, pois precisa lidar com operações de modificação.
# Tupla: Por ser imutável, pode ser mais rápida em operações de acesso ou quando usada como chave em um dicionário.


# 3. Uso como chave em um dicionário

# Lista: Não pode ser usada como chave de um dicionário porque é mutável e, portanto, não tem um hash estável.


# lista = [1, 2, 3]
# dicionario = {lista: "valor"}  # Isso causaria um erro

# Tupla: Pode ser usada como chave de um dicionário porque é imutável e tem um hash estável.

tupla = (1, 2, 3)
dicionario = {tupla: "valor"}
print(dicionario[tupla])  # Saída: valor

# 4. Sintaxe
# Lista: Definida com colchetes [ ].

lista = [1, 2, 3]


# Tupla: Definida com parênteses ( ), mas também pode ser criada sem parênteses.

tupla = (1, 2, 3)
tupla_sem_parenteses = 1, 2, 3

# 5. Semântica de uso
# Lista: É usada quando os dados podem mudar, como em cenários de armazenamento dinâmico.

# Exemplos: Carrinho de compras, lista de tarefas.
# Tupla: É usada quando os dados são constantes ou representam uma estrutura fixa.

# Exemplos: Coordenadas geográficas (latitude, longitude), registros de banco de dados.
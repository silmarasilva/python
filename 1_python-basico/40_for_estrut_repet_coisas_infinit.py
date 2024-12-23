#WHILE
# O while é usado quando não se sabe previamente quantas vezes o laço será executado, mas se tem uma condição que deve ser verdadeira para continuar a repetição.

#Repetir até uma condição ser falsa:

contador = 0
while contador < 5:  # Código a ser executado
    print(contador)
    contador += 1

# Com while: Esperar o usuário digitar "sair":
comando = ""
while comando != "sair":
    comando = input("Digite um comando: ")
    print(f"Você digitou: {comando}")

# Checando senha
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas até que você acerte a senha')

# Usando tamanho da string
texto = 'Python'
i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)
    i += 1

# Usando um while com dicionário
pessoas = {
    "Ana": 25,
    "João": 30,
    "Carlos": 35
}

# Converter o dicionário em uma lista de itens para processar
itens = list(pessoas.items())

# Enquanto houver itens no dicionário
while itens:
    nome, idade = itens.pop(0)  # Remove o primeiro item
    print(f"{nome} tem {idade} anos.")


#FOR
# O for é usado quando se sabe previamente o número de iterações ou se deseja iterar sobre uma sequência (como listas, strings, ou ranges). Ele é mais adequado para percorrer elementos de um iterável.

# Usando tamanho da palavra
texto = 'Python'
for letra in texto:
    print (letra)

# Usando uma lista
nomes = ["Ana", "João", "Carlos"]
for nome in nomes:
    print(nome)

# Iterar usando um range (sequência de números):
for i in range(5):
    print(i)  # Saída: 0, 1, 2, 3, 4

# Usando tamanho da string
texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

# Usando uma dicionário
pessoas = {
    "Ana": 25,
    "João": 30,
    "Carlos": 35
}

# Iterar apenas pelas chaves (nomes)
for nome in pessoas:
    print(nome)

# Iterar pelos valores (idades)
for idade in pessoas.values():
    print(idade)

# Iterar por chaves e valores ao mesmo tempo
for nome, idade in pessoas.items():
    print(f"{nome} tem {idade} anos.")


#O Python itera apenas sobre as chaves do dicionário. Isso ocorre porque a principal estrutura de um dicionário é baseada em pares chave: valor, e a chave é a parte mais acessada por padrão.

# O método .values() retorna apenas os valores armazenados no dicionário, ignorando as chaves.O .values() transforma os valores em algo iterável, permitindo que o for percorra apenas esses valores.

# O método .items() retorna um conjunto de pares chave-valor. Cada par é representado como uma tupla (chave, valor), que pode ser desempacotada em duas variáveis.

# Um método é uma função associada a um objeto que pode ser chamada para realizar uma ação ou obter informações específicas sobre esse objeto. Em Python, métodos são definidos como parte de uma classe, e são usados para interagir com os dados ou funcionalidades que essa classe define.

#A presença dos parênteses () ao chamar um método indica que você está executando a função associada a ele, possivelmente passando argumentos. Eles são necessários porque, sem os parênteses, você estaria apenas referenciando o método, e não executando-o.


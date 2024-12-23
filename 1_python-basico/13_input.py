# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

# Colocar a tipagem diretamente aqui no caso de int efloat poderia quebrar o programa na primeira linha, caso o usuário digitasse uma string.

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
print(f'a soma dos números é" {numero_1 + numero_2}')


# Isso não ocorre com string.

nome = str(input('Qual o seu nome? ')) 
sobrenome  = str(input('Qual o seu sobrenome? '))
print(f'Seu nome completo é {nome} {sobrenome}')

# Aqui estamos jogando a conversão de tipo em um outra variável, então entre o numero_1 e o int_numero_1 eu poderia fazer uma checagem, ou tratar os dados, por exemplo.

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
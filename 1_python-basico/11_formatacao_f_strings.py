#Formatacão de strings com f-strings

nome = 'Silmara Eliza'
altura = 1.58
peso = 56
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

nome = 'Silmara Eliza'
altura = 1.80
peso = 95
imc = peso / altura ** 2

# 2f formata a quantidade de casas decimais.
"f-strings"
linha_1 = f'{nome} tem {altura:2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Silmara Eliza tem 1.58 de altura,
# pesa 56 quilos e seu imc é
# 29.320987654320987
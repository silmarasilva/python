
# Depende da ordem de a, b c

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'a={} b={} c={}'
formato = string.format(a, b, c)
print(formato)

# Usando o número do índice, não dependemos da ordem, a string b pode virar o 0, que no índice é o valor da variável a.

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'a={0} b={1} c={2}'
formato = string.format(a, b, c)
print(formato)

# Usando o f-str para casas decimais.

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)
print(formato)

# Parâmetro nomeado. Tudo que vier depois de um parâmetro precisa ser nomeado. Se eu nomear o C, A e B não precisam ser nomeados, porém se eu nomear A, B e C precisam ser nomeados.

# o valor de c é o argumento, "nome3" é um parâmetro.

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)
print(formato)


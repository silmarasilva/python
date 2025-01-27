# Tipos int e float
# int -> Número Inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado positivo.

print (11) # int
print (-11) # int
print (0) # int


# float -> Número com ponto flutuante.
# O tipo float representa qualquer número.
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.

print(1.1, 10.11) 
print(0.0, -1.6)

# A "funcao" type mostra o tipo que o Python inferiu ao valor.

print( type ('Silmara') ) # Saída: <class 'str'>
print( type ('1') ) # Saída: <class 'str'>
print( type ('1.2'), type(1), type(-1.3), type(0.0) ) # Saída: <class 'str'> <class 'int'> <class 'float'> <class 'float'>



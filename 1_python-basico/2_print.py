# Funcão print com sep -> separador.
# end='\r\n': Insere um "carriage return" (\r) e uma nova linha (\n), comum em sistemas Windows (CRLF).
#\N -> LF
# sep='': Une os valores sem separador, então a saída será 12341011.
# end: Define o que será adicionado ao final da saída. O padrão é uma nova linha ('\n').
# sep: Define o separador entre os valores passados para a função. O padrão é um espaço (' ').

print(12, 34, 1011, sep='', end='\r\n')

print(12, 34, 1011, sep='', end='##\n')
print(12, 34, 1011, sep='', end='\n##')

print(12, 34, sep='-')
print(56, 78)
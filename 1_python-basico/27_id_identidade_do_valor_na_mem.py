"""
Flag (Bandeira) - Marcar um gol.
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""


# id (Identidade do Objeto)
# O que é?
# Cada objeto em Python tem um ID único que representa sua posição na memória.
# A função id() retorna esse número de identidade.

v1 = 'a'
v2 = 'a'
v3 = 'b'
print(id(v1))  # 125814547237744
print(id(v2))  # 125814547237744
print(id(v3))  # 134874496830960

# Análise:
# v1 e v2:

# Ambas as variáveis são atribuídas ao mesmo valor ('a').
# Em Python, strings imutáveis com o mesmo conteúdo podem compartilhar o mesmo local na memória por otimização.
# Resultado: id(v1) == id(v2).
# v3:

# É atribuído a um valor diferente ('b'), então recebe um novo ID.
# Resultado: id(v1) != id(v3).
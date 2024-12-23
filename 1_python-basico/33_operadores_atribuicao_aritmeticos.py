"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

# 1. = (Atribuição simples)
# Usado para definir o valor inicial de uma variável.
# Atribuir um valor
saldo = 1000
print(saldo)  # Saída: 1000


# 2. += (Adicionar e atribuir)
# Comum para incrementar um valor.
# Adicionar pontos a um jogo
pontuacao = 50
pontuacao += 10  # Adiciona 10 à pontuação atual
print(pontuacao)  # Saída: 60


# 3. -= (Subtrair e atribuir)
# Útil para rastrear valores que estão sendo reduzidos.
# Subtrair o valor de um saque do saldo bancário
saldo = 500
saldo -= 100  # Subtrai 100 do saldo
print(saldo)  # Saída: 400


# 4. *= (Multiplicar e atribuir)
# Frequentemente usado em cálculos iterativos.
# Cálculo do crescimento populacional
populacao = 100
taxa_de_crescimento = 1.1  # 10% de crescimento
populacao *= taxa_de_crescimento
print(populacao)  # Saída: 110.0


# 5. /= (Dividir e atribuir)
# Usado para dividir valores acumulados.
# Média de notas
nota_total = 90
numero_de_provas = 3
media = nota_total
media /= numero_de_provas  # Divide pelo número de provas
print(media)  # Saída: 30.0


# 6. //= (Divisão inteira e atribuir)
# Comum para reduzir valores sem precisar de precisão decimal.
# Dividir chocolates igualmente entre pessoas
chocolates = 25
pessoas = 4
chocolates_por_pessoa = chocolates
chocolates_por_pessoa //= pessoas
print(chocolates_por_pessoa)  # Saída: 6


# 7. **= (Exponenciação e atribuir)
# Usado em cálculos exponenciais, como crescimento acelerado.
# Potência de um número
base = 2
expoente = 3
base **= expoente
print(base)  # Saída: 8


# 8. %= (Módulo e atribuir)
# Comum para determinar o restante de uma divisão.
# Determinar se um número é par ou ímpar
numero = 15
numero %= 2  # Resto da divisão por 2
print(numero)  # Saída: 1 (ímpar)

# 1. Iterável
# Um iterável é qualquer objeto que pode ser percorrido, como strings, listas, dicionários, tuplas, e até mesmo o objeto range.
# Para ser considerado iterável, o objeto precisa implementar o método especial __iter__.

texto = "Silmara"  # String
lista = [1, 2, 3]  # Lista

# 2. Iterador
# Um iterador é um objeto que sabe como fornecer os elementos de um iterável um de cada vez.
# Ele deve implementar os métodos especiais __iter__ e __next__:
# __iter__: Retorna o próprio iterador.
# __next__: Retorna o próximo valor do iterador. 
# Quando não houver mais valores, lança a exceção StopIteration.

# 3. iter e next
# iter(objeto): Converte um iterável em um iterador.
# next(iterador): Obtém o próximo valor do iterador.
# Se o iterador não tiver mais elementos, gera uma exceção StopIteration.

# Funcionamento de for no Python
# O loop for automaticamente transforma um iterável em um iterador usando iter e chama next repetidamente até que a exceção StopIteration seja levantada.

# o código abaixo
texto = 'Silmara'  # iterável
for letra in texto:
    print(letra)

# É equivalente a:

# Iterável
texto = "Luiz"

# Criar um iterador a partir do iterável
iterador = iter(texto)  # `__iter__` é chamado internamente aqui

# Loop manual para iterar pelos elementos
while True:
    try:
        letra = next(iterador)  # `__next__` é chamado internamente aqui # Obtém o próximo elemento
        print(letra)
    except StopIteration:
        break  # Sai do loop quando não houver mais elementos


# Saída
# L
# u
# i
# z

# Explicacao

# Explicação do código
# Iterável e Iterador

# texto é um iterável porque é um objeto do tipo str, que implementa o método especial __iter__.
# Quando usamos iter(texto), o método __iter__ é chamado, e ele retorna um iterador. 

# O comando iter(texto) transforma o objeto texto em um iterador.
# Um iterador sabe "lembrar" onde está na sequência e fornece os valores um por um quando chamado com next.

# A função next(iterador) chama o método especial __next__ do iterador, retornando o próximo valor.
# Quando todos os valores forem entregues, o __next__ levanta a exceção StopIteration.
# Tratamento de exceção

# O while True continua chamando next até que a exceção StopIteration seja levantada, momento em que o loop é interrompido.


# O que acontece se tentarmos exibir diretamente o iterador?

texto = iter('Luiz') #__iter__()
print(texto)
# <str_iterator object at 0x7c02d455ae30>

# O iterador não exibe os valores diretamente. Ele é um objeto que precisa ser usado com next ou em loops para fornecer os elementos.

    


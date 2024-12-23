# OBJETOS

# Quase tudo em Python é um objeto, incluindo números, strings, listas, dicionários, funções e até mesmo classes. 
# Um objeto é uma instância de uma classe que pode conter:
# Dados (chamados de atributos ou propriedades).
# Comportamentos (definidos por métodos).

# Números, strings e listas são objetos
numero = 10      # Objeto do tipo int
texto = "Python" # Objeto do tipo str
lista = [1, 2, 3] # Objeto do tipo list

# Cada um desses objetos pertence a uma classe (ex.: int, str, list) que define seus atributos e métodos.

# FUNCÃO

# Uma função é um bloco de código reutilizável que realiza uma tarefa específica. 
# Ela pode receber entradas (parâmetros) e retornar saídas (resultado). 
# Funções podem existir dentro ou fora de classes.

def soma(a, b):  # Definição
    return a + b

resultado = soma(2, 3)  # Chamada
print(resultado)  # Saída: 5

# Características de uma função:

# Pode ser chamada em qualquer lugar do código.
# Não precisa estar vinculada a nenhum objeto ou classe.

# Método
# Um método é uma função vinculada a um objeto. 
# Ele é definido dentro de uma classe e serve para operar nos dados do objeto ou interagir com ele.

class Cachorro:
    def __init__(self, nome):
        self.nome = nome  # Atributo do objeto

    def latir(self):  # Método do objeto
        return f"{self.nome} está latindo!"

# Criar um objeto (instância da classe Cachorro)
meu_cachorro = Cachorro("Rex")

# Chamar o método do objeto
print(meu_cachorro.latir())  # Saída: "Rex está latindo!"

# Diferença-chave entre funções e métodos:

# Função: Existe de forma independente (fora de uma classe).
# Método: Está associado a um objeto (definido dentro de uma classe).
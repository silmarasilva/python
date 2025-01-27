class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        """Inicializa a conta com um saldo inicial."""
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self._saldo = saldo_inicial

    def depositar(self, quantia):
        """Deposita uma quantia positiva na conta."""
        if quantia <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += quantia

    def sacar(self, quantia):
        """Saca uma quantia positiva da conta se houver saldo suficiente."""
        if quantia <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if quantia > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= quantia

    def obter_saldo(self):
        """Obtém o saldo atual."""
        return self._saldo

# Testes de casos limite
def testar_conta_bancaria():
    try:
        print("Testando a classe ContaBancaria...")

        # Testa inicialização com saldos válidos e inválidos
        conta = ContaBancaria(100)
        assert conta.obter_saldo() == 100, "O saldo inicial deve ser 100."

        try:
            ContaBancaria(-10)
        except ValueError as e:
            assert str(e) == "O saldo inicial não pode ser negativo."

        # Testa depósitos
        conta.depositar(50)
        assert conta.obter_saldo() == 150, "O saldo deve ser 150 após o depósito."

        try:
            conta.depositar(-10)
        except ValueError as e:
            assert str(e) == "O valor do depósito deve ser positivo."

        try:
            conta.depositar(0)
        except ValueError as e:
            assert str(e) == "O valor do depósito deve ser positivo."

        # Testa saques
        conta.sacar(50)
        assert conta.obter_saldo() == 100, "O saldo deve ser 100 após o saque."

        try:
            conta.sacar(200)
        except ValueError as e:
            assert str(e) == "Saldo insuficiente."

        try:
            conta.sacar(-10)
        except ValueError as e:
            assert str(e) == "O valor do saque deve ser positivo."

        try:
            conta.sacar(0)
        except ValueError as e:
            assert str(e) == "O valor do saque deve ser positivo."

        print("Todos os testes passaram!")

    except AssertionError as e:
        print(f"Teste falhou: {e}")

# Executa os testes
testar_conta_bancaria()

""""
O código define e testa uma classe ContaBancaria, que simula o funcionamento básico de uma conta bancária. Abaixo está a explicação de cada parte:

Classe ContaBancaria
Esta classe representa uma conta bancária com funcionalidades básicas de depósito, saque e consulta de saldo.

Função testar_conta_bancaria
Testa a funcionalidade da classe ContaBancaria com casos de uso normais e limites (edge cases).

Características de Testes Unitários

Definição:
Testam unidades individuais de código, como funções ou métodos, para garantir que funcionam conforme esperado.

Propósito:
Validar a funcionalidade de partes pequenas e isoladas do sistema (neste caso, os métodos da classe ContaBancaria).

Estrutura:
Um caso de teste avalia um comportamento específico, verificando se a entrada produz a saída esperada ou se as condições esperadas são cumpridas.
Por exemplo:
Testar se o saldo inicial está correto.
Garantir que depósitos inválidos lançam exceções.

Ferramenta Usada no Código:
Utiliza assert diretamente para validar os comportamentos.
Não é uma abordagem formal como as bibliotecas de teste (ex.: unittest ou pytest), mas ainda é válida para pequenos testes informais.

Alternativas Formais
Linguagens como Python oferecem frameworks dedicados para testes unitários, como:

unittest:
Parte da biblioteca padrão de Python.
Mais robusto e com suporte a relatórios detalhados.

pytest:
Popular por sua simplicidade e recursos avançados.
Ideal para projetos maiores.

"""

# Introdução ao try/except em Python
# O bloco try/except é uma das principais ferramentas de tratamento de erros em Python. Ele permite que você "tente" executar um código que pode gerar um erro e forneça uma resposta alternativa caso esse erro ocorra, evitando que o programa seja encerrado inesperadamente.

# try:
#     # Código que pode gerar um erro
# except:
#     # Código que será executado se ocorrer um erro


# Exemplo prático: Dobrar um número digitado pelo usuário:

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    # Tentar converter a entrada do usuário para float
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)  # Exibe o número convertido para float
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')  # Calcula e exibe o dobro
except:
    # Caso ocorra um erro na conversão, exibe uma mensagem ao usuário
    print('Isso não é um número')


# Melhorando a precisão com tipos de erro
# Você pode tornar o tratamento mais específico, lidando apenas com erros que realmente espera, como o ValueError (erro gerado ao tentar converter um texto inválido para número).


numero_str = input('Vou dobrar o número que você digitar: ')
try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except ValueError:
    print('Erro: Você deve digitar um número válido.')

# Vantagem:
# Isso evita que outros tipos de erros (que não têm relação com a conversão) sejam "mascarados".


# Comparação com o uso de isdigit
# A função isdigit() verifica se uma string contém apenas dígitos, mas não suporta números decimais ou negativos

numero_str = input('Vou dobrar o número que você digitar: ')
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Isso não é um número')

# Limitações do isdigit:
# "3.5".isdigit() retorna False (não funciona com decimais).
# "-5".isdigit() retorna False (não funciona com números negativos).
# Por isso, o try/except é mais flexível e geralmente preferível quando se trata de conversão numérica.



# Um exemplo clássico onde o uso de try/except é bem aplicado é na leitura de arquivos. Durante a leitura de um arquivo, vários problemas podem ocorrer, como o arquivo não existir, permissões insuficientes ou até problemas no disco. Usar try/except permite tratar esses cenários sem que o programa seja interrompido abruptamente

# Exemplo: Leitura de Arquivo
# Vamos supor que você deseja ler um arquivo chamado dados.txt e processar seu conteúdo.
# Código com try/except:

try:
    # Tentando abrir o arquivo para leitura
    with open("dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    # Tratamento para caso o arquivo não exista
    print("Erro: O arquivo 'dados.txt' não foi encontrado.")
except PermissionError:
    # Tratamento para caso não tenha permissão para abrir o arquivo
    print("Erro: Permissão negada para acessar 'dados.txt'.")
except Exception as e:
    # Tratamento genérico para outros erros inesperados
    print(f"Erro inesperado: {e}")

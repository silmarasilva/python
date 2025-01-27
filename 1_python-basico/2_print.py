# Exemplo de uso da função print com os argumentos 'sep' e 'end'.

# 1. sep='' -> Une os valores sem nenhum separador.
#    end='\r\n' -> Insere um "carriage return" (\r) e uma nova linha (\n) no final.  O carriage return (abreviado como CR, com o caractere especial representado por \r em muitos sistemas) é um comando de controle utilizado para mover o cursor de texto para o início da linha atual, sem avançar para a próxima linha.
#    (Comum em sistemas Windows para representar o fim de linha - CRLF)
print(12, 34, 1011, sep='', end='\r\n')  # Saída: 12341011

# 2. sep='' -> Une os valores sem separador.
#    end='##\n' -> Adiciona '##' seguido de uma nova linha no final.
print(12, 34, 1011, sep='', end='##\n')  # Saída: 12341011##

# 3. sep='' -> Une os valores sem separador.
#    end='\n##' -> Adiciona uma nova linha seguida de '##' no final.
print(12, 34, 1011, sep='', end='\n##')  # Saída: 12341011 (com \n## no final)

# 4. sep='-' -> Insere um hífen entre os valores passados.
#    end='\n' (padrão) -> Adiciona uma nova linha no final.
print(12, 34, sep='-')  # Saída: 12-34

# 5. Usando os valores padrão de 'sep' (espaço) e 'end' (nova linha).
print(56, 78)  # Saída: 56 78

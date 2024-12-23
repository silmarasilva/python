"""
Interpretador do Python

"""

# # 1. python mod.py
# # Executa um módulo ou script Python.
# # Isso executa o arquivo Python especificado (mod.py) no interpretador.

# python script.py

# # Executa o código contido no arquivo script.py.

# # 2. python -u

# # Isso significa que as saídas padrão (stdout e stderr) não serão armazenadas em buffer. Os dados serão exibidos imediatamente.

# # Saídas padrão (stdout) e erros (stderr) geralmente são armazenados em um "buffer" antes de serem exibidos no terminal.

# # O buffer é uma área temporária de memória usada para melhorar o desempenho, agrupando várias mensagens ou dados antes de enviá-los de uma vez só.

# # Em condições normais, o Python pode segurar a saída no buffer até que:
# # A execução termine.
# # O buffer esteja cheio.
# # Seja explicitamente liberado (como ao imprimir uma nova linha).

# # Com -u, o Python desativa o buffer, garantindo que cada mensagem seja exibida imediatamente no terminal ou gravada no arquivo.

# # Isso é útil em situações onde atrasos na saída podem causar problemas, como:

# # Monitoramento em tempo real: Logs ou mensagens precisam ser exibidos instantaneamente para acompanhar o progresso.
# # Depuração: Você quer ver cada saída à medida que o código é executado.
# # Integração com outras ferramentas: Programas externos que dependem das saídas do Python podem se beneficiar de respostas imediatas.

# # Por que os dados vão para o buffer?
# # Melhorar o desempenho:

# # Operações de entrada e saída (I/O) geralmente envolvem comunicação com dispositivos externos, como discos ou terminais, que são mais lentos do que a memória.
# # O buffer agrupa várias operações pequenas em uma única, reduzindo o número de interações diretas com o dispositivo, tornando o processo mais rápido.
# # Reduzir o custo computacional:

# # Cada operação de I/O tem um custo de processamento associado. Usando um buffer, o sistema pode enviar um grande bloco de dados de uma vez, em vez de enviar cada caractere ou linha separadamente.
# # Evitar congestionamento:

# # Sem o buffer, as operações de saída podem sobrecarregar os recursos do sistema (como o terminal), especialmente em programas que geram muitas mensagens rapidamente.
# # Organização e controle:

# # O buffer permite que o sistema organize e processe os dados antes de exibi-los ou salvá-los, evitando inconsistências.

# # Útil para monitoramento em tempo real, logs ou para evitar atrasos na saída.

# python -u script.py


# # Exibe a saída de script.py imediatamente, sem buffering.

# # 3. python -m mod
# # Executa um módulo como um script.
# # Permite rodar uma biblioteca Python (módulo) como se fosse um script, sem precisar chamá-la explicitamente no código.

# python -m http.server

# # Inicia um servidor HTTP simples na porta 8000.

# # 4. python -c 'cmd'
# # Executa um comando Python diretamente no terminal.
# # Você pode passar um pequeno código Python como string sem precisar de um arquivo .py.

# python -c "print('Olá, mundo!')"
# python -c "print('Olá, mundo\!')"
# python3 -c "print('Olá, mundo\!')"


# # python -i mod.py
# # Executa o script e inicia o modo interativo.

# # O script especificado será executado, e depois o interpretador entrará no modo interativo (prompt >>>).
# # Isso permite inspecionar variáveis e testar código com o estado preservado após a execução do script.

# python -i script.py

# # Após executar o código em script.py, o prompt interativo ficará disponível.

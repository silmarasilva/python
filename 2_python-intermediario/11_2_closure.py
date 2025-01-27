
"""
Funções que retornam outras funções e closures são muito usadas em várias situações práticas, principalmente em programação funcional e em design patterns. Um exemplo comum no desenvolvimento de software é em geradores de funções configuráveis ou funções de filtro personalizadas.

Configuração de Logging

Imagine que você está criando um sistema de logging onde o comportamento do logger pode ser personalizado para diferentes níveis de severidade (como "info", "warn", "error"). Você pode usar funções que retornam outras funções para criar logs personalizados para diferentes contextos sem precisar reescrever a lógica do logger a cada vez.

Aqui está um exemplo de como isso pode ser feito usando closures para configurar o comportamento do logger:
"""

def criar_logger(nivel):
    """
    Função que cria um logger com base no nível de severidade.
    Retorna uma função de log configurada.
    """
    def log(mensagem):
        if nivel == 'info':
            print(f"[INFO]: {mensagem}")
        elif nivel == 'warn':
            print(f"[WARNING]: {mensagem}")
        elif nivel == 'error':
            print(f"[ERROR]: {mensagem}")
        else:
            print(f"[DEBUG]: {mensagem}")

    return log  # Retorna a função log configurada

# Criando diferentes loggers com base no nível de severidade
log_info = criar_logger('info')
log_warn = criar_logger('warn')
log_error = criar_logger('error')

# Usando os loggers configurados
log_info("Sistema iniciado com sucesso.")  # Output: [INFO]: Sistema iniciado com sucesso.
log_warn("O disco está quase cheio.")  # Output: [WARNING]: O disco está quase cheio.
log_error("Falha ao conectar ao banco de dados.")  # Output: [ERROR]: Falha ao conectar ao banco de dados.

# Quando você chama log_info("mensagem"), está passando "mensagem" como argumento para a função log.

"""
Explicação:
A função criar_logger cria e retorna uma função personalizada de logging, que pode ser configurada para diferentes níveis de severidade (como "info", "warn", "error").
O closure é formado porque a função interna log "lembra" o valor do parâmetro nivel da função externa, permitindo que ela se comporte de acordo com o nível de severidade configurado.
Isso elimina a necessidade de escrever várias funções de logging repetitivas e permite que o comportamento de logging seja facilmente configurável em diferentes partes do sistema.

"""
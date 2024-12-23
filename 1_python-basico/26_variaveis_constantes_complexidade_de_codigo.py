"""
CONSTANTE = "Variáveis" que não vão mudar. 
Usar LETRAS_MAIUSCULAS para variáveis que são constantes ao longo do código.
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

# Constantes
RADAR_1 = 60  # Velocidade máxima permitida no radar 1
LOCAL_1 = 100  # Local do radar 1 na estrada
RADAR_RANGE = 1  # Alcance do radar em metros

# Variáveis
velocidade = 61  # Velocidade atual do carro em km/h
local_carro = 100  # Local atual do carro na estrada em metros


# Verificação se o carro está no alcance do radar
carro_no_radar = LOCAL_1 - RADAR_RANGE <= local_carro <= LOCAL_1 + RADAR_RANGE

# Verificação se o carro está acima da velocidade permitida
carro_acima_da_velocidade = velocidade > RADAR_1

# Condicional para emitir uma multa
if carro_no_radar and carro_acima_da_velocidade:
    print("Carro multado! Estava acima da velocidade permitida no radar 1.")
else:
    print("Carro dentro do limite permitido.")


# a variável carro_no_radar analisa se a posicão do carro está no range/alcance que o radar é capaz de captar. Ex. o radar está no kilometro 100 e ele tem alcance de 1km atras e 1km a frente. Então ele só funciona entre os kilometros 99 a 101. Se o carro está no kilometro 100 ele é capaz de alcancar. Então, estando dentro desse rang que o radar alcanca AND acima da velocidade. Ele cai no IF. Se ele não satisfazer essas duas condicoes ele cai no ELSE.





# velocidade_carro_pass_radar_1 = velocidade > RADAR_1

# carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#     local_carro <= (LOCAL_1 + RADAR_RANGE)

# carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_pass_radar_1

# if velocidade_carro_pass_radar_1:
#     print('Velocidade carro passou do radar 1')
# if carro_passou_radar_1:
#     print('Carro passou radar 1')
# if carro_multado_radar_1:
#     print('carro multado em radar 1')

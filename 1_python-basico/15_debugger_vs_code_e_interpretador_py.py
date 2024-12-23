# Debug, ícone com > e um insetinho > "Create a launch.json file > python debugger > arquivo python"
# Com o cursor, marcar no arquivo, ao lado do número da linha (ponto vermelho = breakpoint), onde você quer que o interpretador pare, antes de debbugar.
# No cabecalho, dar play > para iniciar o debug.
# Step Over ele avanca linha por linha. No terminal você consegue ver o que o interpretador está executando.

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')
# solucão 1

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor >= segundo_valor:
    print(f'Primeiro valor={primeiro_valor} é maior ou igual ao segundo_valor {segundo_valor}')
elif segundo_valor >= primeiro_valor:
    print(f'Segundo valor={segundo_valor} é maior ou igual ao primeiro_valor {primeiro_valor}')


# solucão 2 

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )


# Melhor solucão é a 2
# O primeiro exemplo tem redundância no elif porque a condição segundo_valor >= primeiro_valor é implicitamente verdadeira quando a condição if primeiro_valor >= segundo_valor é falsa.


# Segue boas práticas de Python, como:
# Uso de f-strings nomeadas.
# Estrutura clara com apenas dois blocos lógicos (if e else).
# Mensagens mais consistentes e menos redundantes.
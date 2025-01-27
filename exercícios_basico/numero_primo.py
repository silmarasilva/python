# Problema: Verifique se um número é primo.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(17))  # True
print(is_prime(18))  # False


"""

Verificar se o número é menor que 2:
Um número é primo se for maior que 1 e divisível apenas por 1 e ele mesmo.
Exemplos de números primos: 2, 3, 5, 7, 11, 13, 17, etc.
Números menores que 2 (como 0 e 1) não são primos.
Se number < 2, a função imediatamente retorna False

Verificar divisores:
Por que até a raiz quadrada (number ** 0.5)?
Não é necessário testar todos os números até number porque, 
se um número tem um divisor maior que sua raiz quadrada, 
ele também terá um menor. 
Isso reduz o número de iterações, tornando o código mais eficiente.

O range(2, int(number ** 0.5) + 1) 
gera números de 2 até a raiz quadrada de number (incluindo o limite superior).
A cada iteração, verifica-se se number % i == 0, 
ou seja, se há divisores diferentes de 1 e number.
se houver um divisor, o número não é primo e a função retorna False.

Se nenhum divisor foi encontrado no laço for, 
o número é primo, e a função retorna True.

print(is_prime(17))
O número 17 é maior que 2.
A raiz quadrada de 17 é aproximadamente 4,12, então o laço for testa os valores 2, 3 e 4.
Para cada i (2, 3, 4), 17 % i não é 0 (ou seja, 17 não tem divisores).
Nenhum divisor foi encontrado → retorna True.
Saída: True.
print(is_prime(18))
O número 18 é maior que 2.
A raiz quadrada de 18 é aproximadamente 4,24, então o laço for testa os valores 2, 3 e 4.
No primeiro teste (i = 2), 18 % 2 == 0 (18 é divisível por 2).
O número não é primo → retorna False.
Saída: False.

"""

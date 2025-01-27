'''
Problema: Gere uma senha aleatória com tamanho e tipos de caracteres configuráveis.

'''

import random
import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

print(generate_password(12)) # Exemplo: !8a&B@1k$d#



# random.choice(), é usada aqui para escolher aleatoriamente caracteres de uma sequência.
# string.ascii_letters: Contém todas as letras do alfabeto (tanto maiúsculas quanto minúsculas). 
# string.digits: Contém todos os dígitos de 0 a 9. Exemplo: '0123456789'.
# string.punctuation: Contém todos os caracteres de pontuação, como !"#$%&'()*+,-./:;<=>?@[\]^_{|}~`.


# ''.join(...): A função join() é usada para unir os caracteres escolhidos aleatoriamente em uma única string.
# for _ in range(length): Um loop que vai se repetir length vezes. Cada vez, o random.choice(chars) escolhe um caractere aleatório.
# O uso de _ como variável de iteração é uma convenção quando você não precisa do valor da variável.

'''
Problema: Verifique se uma palavra é um palíndromo (lê-se da mesma forma de trás para frente).
'''

def is_palindrome(word):
    word = word.lower().replace(" ", "")  # Converte tudo para minúsculas e remove espaços.
    return word == word[::-1] # Compara a string com sua inversa.

print(is_palindrome("arara"))  # True
print(is_palindrome("Python"))  # False


# fatiamento (slicing) 
# sequencia[inicio:fim:passo]



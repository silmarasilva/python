'''
Problema: Conte a frequência de cada palavra em um texto fornecido.

'''

from collections import Counter

def word_frequency(text):
    words = text.lower().split()
    return Counter (words)

text = "PYthon é divertido. Python é poderoso"
print (word_frequency(text))

# Counter({'python': 2, 'é': 2, 'divertido.': 1, 'poderoso.': 1})

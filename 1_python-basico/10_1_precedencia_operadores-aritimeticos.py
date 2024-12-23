# 1. (n + n)    ->  coisas dentro de parênteses
# 2. **         -> expoenntes
# 3. * / // %   -> multiplicacão, divísão, divisão inteira e módulo.
# 4. + -        -> subtracao e adicão


#7
conta_1 = (1 + 1 ** 5 + 5)
print (conta_1)

#1024
conta_1 = ((1 + 1) ** (5 + 5))
print (conta_1)

#1024 
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)
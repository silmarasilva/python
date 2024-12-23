# Conversão de tipos, coercão. 
# Type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos: str, int, float, bool

print (1 + 1) # somou 
print ('a' + 'b')  # concatenou


print ('1' + 1) # TypeError: can only concatenate str (not "int") to str. Nesse caso ele não converte pq o python possui tipagem forte. 

# Se fosse uma linguagem de tipagem fraca ele varia a conversão. No JavaScript, por exemplo, ele faria: console.log('1' + 1);  // Saída: '11'. No PHP <?php echo '1' + 1;  // Saída: 2 ?>

# Em contraste, linguagens como Python com tipagem forte exigem que você converta explicitamente os tipos quando necessário.


print ('1', type('1'))

# coercão de str em int.
print (int('1'), type(int('1'))) 
print  (int('1') + 1)

# coercão de str em float.
print (float("1")+ 1)
print (type(float("1")+ 1))

# coercão de int em str.
print (str(11) + 'b')

#String Vazia é considerada False
print (bool(''))


# O polimorfismo é um conceito fundamental da programação orientada a objetos (OOP) que permite que objetos de diferentes classes sejam tratados de forma uniforme, desde que compartilhem uma interface comum. Em Python, o polimorfismo é altamente flexível devido à sua tipagem dinâmica e ao suporte à herança e composição.

#Definição Simples: Polimorfismo significa "muitas formas". Em termos práticos, refere-se à capacidade de usar uma mesma interface para objetos de diferentes tipos. Isso permite que você escreva código mais genérico e reutilizável.
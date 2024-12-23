# O método .count() de strings é bastante comum em cenários que envolvem análise e manipulação de textos. Aqui estão algumas situações práticas em que esse método é utilizado:

# Usado para identificar a frequência de palavras ou caracteres em textos. Por exemplo:
# Contar palavras-chave em um artigo para SEO.
# Identificar caracteres ou palavras recorrentes em análises de dados textuais.


texto = "Python é divertido. Python é poderoso. Python é simples."
palavra = "Python"
print(f'A palavra "{palavra}" aparece {texto.count(palavra)} vezes.')


texto = "Python é divertido. Python é poderoso. Python é simples."
letra = "P"
print(f'A letra "{letra}" aparece {texto.count(letra)} vezes.')


# Processamento de Logs ou Dados de Sistemas:
# Contar a ocorrência de termos específicos, como mensagens de erro ou códigos de status, em logs.


log = "ERROR: conexão falhou\nINFO: Tentando novamente\nERROR: Timeout."
print(f'Erro apareceu {log.count("ERROR")} vezes.')


# Verificação de Simbolismo em Arquivos ou Textos:
# Para garantir que caracteres ou símbolos específicos aparecem o número esperado de vezes, como em validação de strings em senhas ou formato de documentos.

senha = "abc@123@!"
print(f'O símbolo "@" aparece {senha.count("@")} vezes.')


# Este tipo de abordagem é útil em processamento básico de strings antes de usar bibliotecas mais avançadas, como collections.Counter ou pandas.
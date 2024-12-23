# for

# Número de iterações conhecido: Iterações é conhecido ou iterável é definido.
# Dependência de uma condição: Itera automaticamente sobre um iterável.
# Clareza do código: Mais legível e conciso para iterar sequências.

# Lista de contatos para envio de emails
contatos = ["ana@example.com", "joao@example.com", "carlos@example.com"]

for email in contatos:
    print(f"Enviando email para {email}...")
    # Simula o envio do email
    # enviar_email(email)
    print("Email enviado com sucesso!")


# while
# Número de iterações conhecido: Usado quando não se sabe o número de iterações.
# Dependência de uma condição: Continua enquanto a condição for verdadeira.
# Clareza do código: Útil para loops baseados em lógica condicional.

contatos = ["ana@example.com", "joao@example.com", "carlos@example.com"]
indice = 0

while indice < len(contatos):
    email = contatos[indice]
    print(f"Enviando email para {email}...")
    # Simula uma condição para erro
    if email == "joao@example.com":
        print("Erro no envio. Parando o processo.")
        break
    print("Email enviado com sucesso!")
    indice += 1

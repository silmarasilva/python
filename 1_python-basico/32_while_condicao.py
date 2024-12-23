"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0
while contador <= 10:
    contador = contador + 1
    print(contador)
print('Acabou')


# Exemplo: Menu interativo para cadastro de itens
itens = []

while True:  # Loop infinito até o usuário escolher "Sair"
    print("\nMENU:")
    print("1. Adicionar item")
    print("2. Listar itens")
    print("3. Sair")
    
    escolha = input("Escolha uma opção (1, 2, ou 3): ")
    
    if escolha == "1":
        item = input("Digite o nome do item a ser adicionado: ")
        itens.append(item)
        print(f"'{item}' foi adicionado com sucesso!")
    elif escolha == "2":
        if itens:  # Verifica se a lista contém itens
            print("Itens cadastrados:")
            for i, item in enumerate(itens, start=1):  # Enumera os itens para melhor visualização
                print(f"{i}. {item}")
        else:
            print("Nenhum item cadastrado ainda.")  # Mensagem quando a lista está vazia
    elif escolha == "3":
        print("Encerrando o programa. Até mais!")
        break  # Sai do loop
    else:
        print("Opção inválida! Tente novamente.")

print("Programa finalizado.")
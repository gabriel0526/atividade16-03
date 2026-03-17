tarefas = []

while True: 
    print("\n=== TASK MANAGER v1.0 ===")
    print("1 - criar tarefa")
    print("2 - listar tarefas")
    print("3 - deletar tarefas")
    print("4 - sair")
    
    opcao = input("\nescolha uma opção: ")

    if opcao not in  ["1", "2", "3", "4"]:
        print("x opção inválida! Digite 1, 2, 3 ou 4")

    if opcao == "1":
        nome = input("nome da tarefa: ")
        if nome.strip():
            tarefas.append(nome)
            print(f"Tarefa {nome} criada com sucesso!")
        else:
            print("x nome da tarefa não pode ser vazio")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("nenhuma tarefa registrada ainda")
        else:
            print("\nSuas tarefas")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}, {tarefas}")

    elif opcao == "3":
        indice = input("qual tarefa deletar (numero)? ")
        if indice.isdigit() and 0 

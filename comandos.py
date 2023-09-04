import sqlite3
import gerenciador 

while True:
    print("\n >>> Sistema de Gerenciamento de Tarefas <<< ")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Excluir Tarefa")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        task = input("Digite aqui sua nova tarefa: ")
        gerenciador.adicionar_tarefa(task)
        print("Tarefa adicionada com sucesso!")
    elif escolha == '2':
        tasks = gerenciador.listar_tarefas()
        for task in tasks:
            print(f"{task[0]}. {task[1]} {'(Concluída)' if task[2] else ''}")
    elif escolha == '3':
        task_id = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
        gerenciador.marcar_como_concluida(task_id)
        print("Tarefa marcada como concluída!")
    elif escolha == '4':
        task_id = int(input("Digite o ID da tarefa a ser excluída: "))
        gerenciador.excluir_tarefa(task_id)
        print("Tarefa excluída com sucesso!")
    elif escolha == '0':
        print("Tchau, até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

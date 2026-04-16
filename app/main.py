from app.handlers import (
    handle_add_task,
    handle_remove_task,
    handle_update_task,
    handle_complete_task,
    list_tasks
)


# Exibe o menu principal do sistema
def menu():
    print("\n" + "=" * 40)
    print("TASK MANAGER CLI")
    print("=" * 40)
    print("1 - Add Task")
    print("2 - Remove Task")
    print("3 - Update Task Priority")
    print("4 - Show Tasks")
    print("5 - Complete Task")
    print("6 - Exit")
    print("=" * 40)


# Mapeia opções para funções do sistema
options = {
    2: handle_remove_task,
    3: handle_update_task,
    4: list_tasks,
    5: handle_complete_task
}


# Processa a opção escolhida pelo usuário
def handle_option(choice, tasks, task_id):
    if choice == 1:
        return handle_add_task(tasks, task_id)
    
    elif choice in options:
        options[choice](tasks)
        return task_id
    
    else:
        print("Please choose a valid option.")
        return task_id


# Loop principal do sistema
def run():
    # Lista de tarefas do sistema
    tasks = []
    
    # Controle do próximo ID de tarefa
    task_id = 1

    while True:
        menu()

        try:
            choice = int(input("Choose an option: "))

            if choice == 6:
                print("Goodbye!")
                break

            task_id = handle_option(choice, tasks, task_id)

        except ValueError:
            print("Please enter a valid number.")
from app.logic import *
from app.utils import get_task_id


def handle_add_task(tasks, task_id):
    # Coleta dados básicos da tarefa via input do usuário
    name = input("Insert the task name: ").strip().lower()
    
    try:
        # Prioridade da tarefa (controle de importância)
        priority = int(input("Choose a task priority (1- lowest, 5 - highest): "))
    except ValueError:
        print("Invalid priority.")
        return
    
    # Cria a estrutura da tarefa usando lógica central do sistema
    task = create_task(name, priority, task_id)
    
    # Adiciona a tarefa na lista principal
    add_task(tasks, task)
    
    # Retorna o próximo ID disponível
    return task_id + 1 


def handle_remove_task(tasks):
    # Mostra tarefas antes de remover para facilitar escolha do usuário
    list_tasks(tasks)

    # Captura ID da tarefa que será removida
    task_id = get_task_id()

    if task_id is None:
        return
    
    # Tenta remover e valida resultado
    if delete_task(tasks, task_id):
        print("Task removed successfully.")
    else:
        print("Task not found")


def handle_update_task(tasks):
    # Lista tarefas para o usuário escolher corretamente
    list_tasks(tasks)
    
    task_id = get_task_id()
    
    if task_id is None:
        return
    
    try:
        # Nova prioridade para atualização da tarefa
        new_priority = int(input("Choose a task priority (1- lowest, 5 - highest): "))
    except ValueError:
        print("Invalid priority")
        return
    
    # Atualiza prioridade da tarefa selecionada
    if update_task_priority(tasks, task_id, new_priority):
        print("Task updated successfully.")
    else:
        print("Task not found.")


def handle_complete_task(tasks):
    # Lista tarefas antes da seleção
    list_tasks(tasks)
    
    task_id = get_task_id()
    
    if task_id is None:
        return

    # Marca tarefa como concluída
    if complete_task(tasks, task_id):
        print("Task completed successfully.")
    else:
        print("Task not found.")


# Function to display all tasks
def list_tasks(tasks):
    # Verifica se existem tarefas antes de tentar exibir
    if not tasks:
        print("No tasks registered.")
        return

    print("\n=== TASK LIST ===\n")

    # Exibe cada tarefa com status formatado
    for task in tasks:
        status = "✔ Done" if task["done"] else "✖ Pending"
        print(f"[{task['id']}] {task['name']} | Priority: {task['priority']} | {status}")
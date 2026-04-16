# Solicita e captura o ID da tarefa escolhido pelo usuário
def get_task_id():
    try:
        task_id = int(input("Choose the task id."))
        return task_id
    except ValueError:
        # Caso o usuário digite algo que não seja número
        print("Invalid id")
        return None
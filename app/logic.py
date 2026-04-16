# Cria uma nova estrutura de tarefa
def create_task(name, priority, next_id):
    task = {
        "id": next_id,
        "name": name,
        "priority": priority,
        "done": False
    }

    return task


# Adiciona uma tarefa na lista principal
def add_task(tasks, task):
    tasks.append(task)
    return tasks


# Remove uma tarefa pelo ID
def delete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return True

    return False


# Atualiza a prioridade de uma tarefa
def update_task_priority(tasks, task_id, new_priority):
    for task in tasks:
        if task['id'] == task_id:
            task['priority'] = new_priority
            return True

    return False


# Marca uma tarefa como concluída
def complete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            return True

    return False
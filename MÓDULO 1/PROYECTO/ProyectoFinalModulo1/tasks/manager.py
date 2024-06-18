from .storage import load_tasks, save_tasks

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)

def get_tasks():
    return load_tasks()

def delete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)

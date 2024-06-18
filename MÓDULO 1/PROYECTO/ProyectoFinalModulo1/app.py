import streamlit as st
from tasks.manager import add_task, get_tasks, delete_task

def main():
    st.title("Gestor de Tareas")

    st.header("Agregar Tarea")
    new_task = st.text_input("Nueva Tarea:")
    if st.button("Agregar"):
        if new_task:
            add_task(new_task)
            st.success(f"Tarea '{new_task}' agregada!")
        else:
            st.error("La tarea no puede estar vacía.")

    st.header("Tareas")
    tasks = get_tasks()
    if tasks:
        for i, task in enumerate(tasks):
            st.write(f"{i + 1}. {task['task']}")
    else:
        st.write("No hay tareas disponibles.")

    st.header("Eliminar Tarea")
    if tasks:
        task_index = st.number_input("Número de la Tarea a Eliminar", min_value=1, max_value=len(tasks), step=1)
        if st.button("Eliminar"):
            delete_task(task_index - 1)
            st.success(f"Tarea {task_index} eliminada!")
    else:
        st.write("No hay tareas para eliminar.")

if __name__ == "__main__":
    main()

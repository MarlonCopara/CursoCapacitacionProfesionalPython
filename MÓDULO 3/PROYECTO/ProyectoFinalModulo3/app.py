import streamlit as st
from employee import RegularEmployee, Manager

# Lista para almacenar los empleados
employee_list = []

# Configuración de la página
st.set_page_config(page_title="Gestión de Empleados", layout="wide")

# Función para mostrar la interfaz principal
def main():
    global employee_list  # Acceder a la lista de empleados globalmente
    
    st.title("Sistema de Gestión de Empleados")

    # Crear columnas para organizar mejor la interfaz
    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("Agregar Nuevo Empleado")
        emp_type = st.radio("Tipo de Empleado:", ("Regular", "Gerente"))
        name = st.text_input("Nombre:")
        salary = st.number_input("Salario:", min_value=0.0)

        if st.button("Agregar Empleado"):
            try:
                if emp_type == "Regular":
                    employee = RegularEmployee(name, salary)
                elif emp_type == "Gerente":
                    employee = Manager(name, salary)
                
                employee_list.append(employee)  # Agregar empleado a la lista
                st.success(f"Empleado '{employee.name}' agregado correctamente.")
                st.subheader("Detalles del Empleado Agregado:")
                st.write(employee.get_details())

            except ValueError as e:
                st.error(f"Error: {e}")

    with col2:
        st.header("Lista de Empleados")

        # Mostrar lista de empleados
        for idx, employee in enumerate(employee_list):
            with st.expander(f"{employee.name} - Salario: {employee.salary:.2f}"):
                st.write(f"Tipo: {'Gerente' if isinstance(employee, Manager) else 'Regular'}")
                st.write(employee.get_details())

                # Botón para eliminar empleado
                if st.button(f"Eliminar {employee.name}"):
                    del employee_list[idx]
                    st.warning(f"Empleado '{employee.name}' eliminado.")

# Función principal para ejecutar la aplicación
if __name__ == "__main__":
    main()

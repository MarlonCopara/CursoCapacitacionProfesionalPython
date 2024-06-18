import streamlit as st
from contact_functions import *

def main():
    st.title("Gestor de Contactos")

    st.header("Agregar Nuevo Contacto")
    name = st.text_input("Nombre:")
    phone = st.text_input("Teléfono:")
    email = st.text_input("Correo Electrónico:")

    if st.button("Agregar Contacto"):
        if name and phone and email:
            add_contact(name, phone, email)
            st.success(f"Contacto '{name}' agregado correctamente.")
        else:
            st.warning("Por favor, complete todos los campos.")

    st.header("Buscar Contacto por Nombre")
    search_name = st.text_input("Ingrese el nombre del contacto a buscar:")
    
    if st.button("Buscar"):
        if search_name:
            contact_info = find_contact(search_name)
            if contact_info:
                st.write(f"Nombre: {contact_info['name']}")
                st.write(f"Teléfono: {contact_info['phone']}")
                st.write(f"Correo Electrónico: {contact_info['email']}")
            else:
                st.warning(f"No se encontró el contacto '{search_name}'.")
        else:
            st.warning("Ingrese un nombre para buscar.")

    st.header("Actualizar Contacto")
    update_name = st.text_input("Ingrese el nombre del contacto a actualizar:")
    update_phone = st.text_input("Nuevo Teléfono:")
    update_email = st.text_input("Nuevo Correo Electrónico:")

    if st.button("Actualizar"):
        if update_name and (update_phone or update_email):
            updated = update_contact(update_name, update_phone, update_email)
            if updated:
                st.success(f"Contacto '{update_name}' actualizado correctamente.")
            else:
                st.warning(f"No se encontró el contacto '{update_name}'.")
        else:
            st.warning("Ingrese el nombre del contacto y al menos uno de los campos para actualizar.")

    st.header("Eliminar Contacto")
    delete_name = st.text_input("Ingrese el nombre del contacto a eliminar:")

    if st.button("Eliminar"):
        if delete_name:
            deleted = delete_contact(delete_name)
            if deleted:
                st.success(f"Contacto '{delete_name}' eliminado correctamente.")
            else:
                st.warning(f"No se encontró el contacto '{delete_name}'.")
        else:
            st.warning("Ingrese el nombre del contacto a eliminar.")

if __name__ == "__main__":
    main()

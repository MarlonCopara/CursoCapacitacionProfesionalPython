import streamlit as st
import subprocess

# Funciones para manejar módulos y paquetes
def create_module(module_name, content):
    with open(f"{module_name}.py", "w") as file:
        file.write(content)

def create_package(package_name, module_name, content):
    import os
    os.makedirs(package_name, exist_ok=True)
    with open(os.path.join(package_name, "__init__.py"), "w") as file:
        file.write("# Init file for the package\n")
    with open(os.path.join(package_name, f"{module_name}.py"), "w") as file:
        file.write(content)

# Funciones para pip
def install_package(package_name):
    subprocess.run(["pip", "install", package_name])

def list_installed_packages():
    installed_packages = subprocess.run(["pip", "list"], capture_output=True, text=True)
    return installed_packages.stdout

# Contenido de ejemplo
example_module_content = """
def hello_world():
    return "Hello, world!"
"""

example_package_module_content = """
def greet(name):
    return f"Hello, {name}!"
"""

# Main Streamlit app
def main():
    st.title("Python Modules, Packages, and pip")

    st.header("Módulo 1: Módulos")
    st.write("Un módulo en Python es un archivo que contiene definiciones y declaraciones de Python.")
    module_name = st.text_input("Nombre del módulo:")
    if st.button("Crear Módulo"):
        create_module(module_name, example_module_content)
        st.success(f"Módulo {module_name}.py creado con éxito!")

    st.header("Módulo 2: Paquetes")
    st.write("Un paquete es una colección de módulos organizados en directorios con un archivo __init__.py.")
    package_name = st.text_input("Nombre del paquete:")
    package_module_name = st.text_input("Nombre del módulo del paquete:")
    if st.button("Crear Paquete"):
        create_package(package_name, package_module_name, example_package_module_content)
        st.success(f"Paquete {package_name} con módulo {package_module_name}.py creado con éxito!")

    st.header("Módulo 3: pip")
    st.write("pip es la herramienta de Python para instalar y gestionar paquetes.")
    package_to_install = st.text_input("Nombre del paquete a instalar con pip:")
    if st.button("Instalar paquete"):
        install_package(package_to_install)
        st.success(f"Paquete {package_to_install} instalado con éxito!")

    if st.button("Listar paquetes instalados"):
        packages = list_installed_packages()
        st.text(packages)

if __name__ == "__main__":
    main()

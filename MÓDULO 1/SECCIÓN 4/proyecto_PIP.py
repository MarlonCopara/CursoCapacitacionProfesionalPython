import streamlit as st
import subprocess

def install_package(package_name):
    subprocess.run(["pip", "install", package_name])

def list_installed_packages():
    installed_packages = subprocess.run(["pip", "list"], capture_output=True, text=True)
    return installed_packages.stdout

def check_dependencies(package_name):
    result = subprocess.run(["pip", "show", package_name], capture_output=True, text=True)
    return result.stdout

def main():
    st.title("Python Package Installer (pip)")

    st.header("1.4.1 El Ecosistema de Paquetes de Python y cómo usarlo")
    st.write("Python tiene un vasto ecosistema de paquetes disponibles en PyPI (Python Package Index) que permite a los desarrolladores compartir y usar librerías.")

    st.header("1.4.2 El Repositorio de PyPI: la Tienda de Quesos")
    st.write("PyPI es el repositorio oficial para software de terceros para Python. Puedes buscar paquetes y leer su documentación en [PyPI](https://pypi.org).")

    st.header("1.4.3 Cómo instalar pip")
    st.write("pip suele estar instalado por defecto con Python. Si no lo tienes, puedes instalarlo usando `ensurepip`:")
    st.code("python -m ensurepip --upgrade")

    st.header("1.4.4 Dependencias")
    st.write("Las dependencias son otros paquetes que un paquete necesita para funcionar correctamente. pip maneja automáticamente las dependencias al instalar un paquete.")

    st.header("1.4.5 Cómo usar pip")
    st.write("Usa el siguiente comando para instalar un paquete:")
    st.code("pip install nombre_del_paquete")

    st.header("1.4.6 Un programa de prueba simple")
    st.write("Vamos a crear un programa que instale un paquete y liste los paquetes instalados.")

    st.header("1.4.7 ¡Utiliza pip!")
    package_name = st.text_input("Nombre del paquete a instalar:")
    if st.button("Instalar paquete"):
        install_package(package_name)
        st.success(f"Paquete {package_name} instalado exitosamente!")

    if st.button("Listar paquetes instalados"):
        packages = list_installed_packages()
        st.text(packages)

    st.header("1.4.8 RESUMEN DE SECCIÓN")
    st.write("""
    - PyPI es el repositorio oficial de paquetes de Python.
    - pip es la herramienta para instalar y gestionar paquetes de Python.
    - Puedes instalar pip usando `ensurepip`.
    - pip maneja automáticamente las dependencias.
    - Puedes usar pip para instalar, listar y manejar paquetes.
    """)

  
if __name__ == "__main__":
    main()

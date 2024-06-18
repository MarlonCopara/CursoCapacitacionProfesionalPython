
import streamlit as st
import math
import random
import platform

def main():
    st.title("Demostración de Módulos Selectos de Python")

    st.header("1.2.1 Trabajando con módulos estándar")
    raiz_cuadrada = math.sqrt(16)
    st.write(f"La raíz cuadrada de 16 es: {raiz_cuadrada}")

    st.header("1.2.2 Funciones selectas del módulo math")
    valor_pi = math.pi
    seno_pi_medios = math.sin(math.pi / 2)
    logaritmo_natural = math.log(1)
    st.write(f"El valor de pi es: {valor_pi}")
    st.write(f"El seno de pi/2 es: {seno_pi_medios}")
    st.write(f"El logaritmo natural de 1 es: {logaritmo_natural}")

    st.header("1.2.3 ¿Existe aleatoriedad real en las computadoras?")
    st.write("Las computadoras generan números pseudoaleatorios usando algoritmos deterministas.")

    st.header("1.2.4 Funciones selectas del módulo random")
    numero_aleatorio = random.random()
    entero_aleatorio = random.randint(1, 10)
    eleccion_aleatoria = random.choice(['manzana', 'banana', 'cereza'])
    st.write(f"Número aleatorio entre 0 y 1: {numero_aleatorio}")
    st.write(f"Número entero aleatorio entre 1 y 10: {entero_aleatorio}")
    st.write(f"Elección aleatoria de una lista: {eleccion_aleatoria}")

    st.header("1.2.5 ¿Cómo saber dónde estás?")
    st.write("El módulo platform se usa para acceder a la información del sistema operativo y la plataforma en la que se ejecuta Python.")

    st.header("1.2.6 Funciones selectas del módulo platform")
    sistema_operativo = platform.system()
    version_sistema = platform.version()
    arquitectura = platform.machine()
    st.write(f"Sistema operativo: {sistema_operativo}")
    st.write(f"Versión del sistema operativo: {version_sistema}")
    st.write(f"Arquitectura de la máquina: {arquitectura}")

if __name__ == "__main__":
    main()

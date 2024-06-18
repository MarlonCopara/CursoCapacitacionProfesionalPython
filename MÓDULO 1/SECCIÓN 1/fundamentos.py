# streamlit_app.py
import streamlit as st
import math
from math import sqrt, sin, pi

def main():
    st.title("Demostración de Módulos en Python")

    if st.button('Usar mi_modulo'):
        st.write("¡Hola desde el módulo!")

    st.header("Uso del módulo Math")
    st.write(f"La raíz cuadrada de 16 es {math.sqrt(16)}")
    
    st.header("Importando partes específicas de un módulo")
    st.write(f"La raíz cuadrada de 25 es {sqrt(25)}")
    
    st.header("Importando todo el contenido de un módulo")
    st.write(f"El seno de π/2 es {sin(pi / 2)}")
    
    st.header("Renombrando un módulo")
    import math as m
    st.write(f"La raíz cuadrada de 36 es {m.sqrt(36)}")
    
    st.header("Alias en importaciones")
    from math import sqrt as raiz_cuadrada
    st.write(f"La raíz cuadrada de 49 es {raiz_cuadrada(49)}")

if __name__ == "__main__":
    main()

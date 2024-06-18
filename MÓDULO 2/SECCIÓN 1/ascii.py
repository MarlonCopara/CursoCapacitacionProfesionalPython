import streamlit as st

def ascii_table():
    ascii_values = list(range(32, 127))
    ascii_chars = [chr(value) for value in ascii_values]
    ascii_table = dict(zip(ascii_values, ascii_chars))
    return ascii_table

def main():
    st.title("Tabla de Caracteres ASCII")

    ascii_table_data = ascii_table()

    st.header("Caracteres ASCII Imprimibles")
    st.write("Aquí están los caracteres ASCII imprimibles del 32 al 126:")

    for value, char in ascii_table_data.items():
        st.write(f"{value}: {char}")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os

# Función para cargar los eventos desde un archivo CSV
def load_events():
    try:
        events_df = pd.read_csv("events.csv", parse_dates=['date'])  # Parseamos la columna 'date' como fecha
        if events_df.empty:
            events_list = []
        else:
            events_list = events_df.to_dict("records")
            for event in events_list:
                event['image_path'] = event.get('image_path', '')  # Aseguramos que 'image_path' exista en cada evento
    except (FileNotFoundError, pd.errors.EmptyDataError):
        events_list = []
    
    return events_list

# Función para guardar los eventos en un archivo CSV
def save_events(events):
    events_df = pd.DataFrame(events)
    events_df.to_csv("events.csv", index=False)

# Función para agregar un nuevo evento
def add_event(event_name, event_date, event_description, event_image):
    # Guardar la imagen
    if event_image is not None:
        image_path = save_event_image(event_image, event_name)
    else:
        image_path = ''
        
    events.append({
        "name": event_name,
        "date": event_date,
        "description": event_description,
        "image_path": image_path
    })
    save_events(events)

# Función para guardar la imagen de un evento
def save_event_image(event_image, event_name):
    # Crear directorio si no existe
    if not os.path.exists('event_images'):
        os.makedirs('event_images')
    
    # Guardar la imagen en un archivo
    image_path = f"event_images/{event_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
    with open(image_path, 'wb') as f:
        f.write(event_image.read())
    
    return image_path

# Función para editar un evento existente
def edit_event(index, event_name, event_date, event_description, event_image):
    # Eliminar la imagen anterior si se cambia
    if event_image is not None:
        old_image_path = events[index]['image_path']
        if old_image_path:
            os.remove(old_image_path)
        new_image_path = save_event_image(event_image, event_name)
    else:
        new_image_path = events[index]['image_path']
    
    # Actualizar el evento
    events[index] = {
        "name": event_name,
        "date": event_date,
        "description": event_description,
        "image_path": new_image_path
    }
    save_events(events)

# Función para eliminar un evento existente
def delete_event(index):
    deleted_event = events.pop(index)
    # Eliminar la imagen asociada
    image_path = deleted_event.get('image_path', '')
    if image_path and os.path.exists(image_path):
        os.remove(image_path)
    save_events(events)
    return deleted_event

# Función para mostrar los eventos
def show_events():
    if events:
        st.write("### Lista de Eventos:")
        for idx, event in enumerate(events, start=1):
            if isinstance(event['date'], datetime):
                formatted_date = event['date'].strftime('%Y-%m-%d')
            else:
                formatted_date = event['date']
            
            st.write(f"**{event['name']}**")
            st.write(f"Fecha: {formatted_date}")
            st.write(f"Descripción: {event['description']}")
            if event['image_path']:
                st.image(event['image_path'], caption='Imagen del Evento', use_column_width=True)
            else:
                st.write("No hay imagen asociada.")
            st.write("---")
    else:
        st.write("No hay eventos programados.")

def main():
    global events
    st.title("Sistema de Gestión de Eventos")

    # Cargar eventos al inicio de la aplicación
    events = load_events()

    menu = ["Ver Eventos", "Agregar Evento", "Editar Evento", "Eliminar Evento"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Ver Eventos":
        show_events()

    elif choice == "Agregar Evento":
        st.header("Agregar Nuevo Evento")
        event_name = st.text_input("Nombre del Evento")
        event_date = st.date_input("Fecha del Evento", min_value=datetime.now() + timedelta(days=1))
        event_description = st.text_area("Descripción del Evento")
        event_image = st.file_uploader("Cargar Imagen del Evento", type=['jpg', 'jpeg', 'png'])

        if st.button("Agregar Evento"):
            add_event(event_name, event_date, event_description, event_image)
            st.success(f"Evento '{event_name}' agregado para el {event_date.strftime('%Y-%m-%d')}")
            st.info("Puedes ver todos los eventos en la sección 'Ver Eventos'")

    elif choice == "Editar Evento":
        st.header("Editar Evento Existente")
        if events:
            event_options = [event["name"] for event in events]
            selected_event = st.selectbox("Selecciona un Evento", event_options)

            if selected_event:
                index = event_options.index(selected_event)
                event_name = st.text_input("Nuevo nombre del Evento", value=events[index]["name"])
                event_date = st.date_input("Nueva fecha del Evento", value=events[index]["date"])
                event_description = st.text_area("Nueva descripción del Evento", value=events[index]["description"])
                event_image = st.file_uploader("Cargar Nueva Imagen del Evento", type=['jpg', 'jpeg', 'png'])

                if st.button("Guardar Cambios"):
                    edit_event(index, event_name, event_date, event_description, event_image)
                    st.success(f"Evento '{selected_event}' editado correctamente.")
                    st.info("Puedes ver todos los eventos en la sección 'Ver Eventos'")
        else:
            st.write("No hay eventos para editar.")

    elif choice == "Eliminar Evento":
        st.header("Eliminar Evento Existente")
        if events:
            event_options = [event["name"] for event in events]
            selected_event = st.selectbox("Selecciona un Evento para eliminar", event_options)

            if st.button("Eliminar Evento"):
                index = event_options.index(selected_event)
                deleted_event = delete_event(index)
                st.success(f"Evento '{selected_event}' eliminado correctamente.")
                st.info("Puedes ver todos los eventos en la sección 'Ver Eventos'")
        else:
            st.write("No hay eventos para eliminar.")

if __name__ == "__main__":
    main()

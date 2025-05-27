import streamlit as st

# Lista de departamentos
departamentos = [
    "Amazonas", "Antioquia", "Arauca", "Atlántico", "Bolívar", "Boyacá", "Caldas",
    "Caquetá", "Casanare", "Cauca", "Cesar", "Chocó", "Cundinamarca", "Córdoba",
    "Guainía", "Guaviare", "Huila", "La Guajira", "Magdalena", "Meta", "Nariño",
    "Norte de Santander", "Putumayo", "Quindío", "Risaralda",
    "San Andrés Providencia y Santa Catalina", "Santander", "Sucre", "Tolima",
    "Valle del Cauca", "Vaupés", "Vichada"
]

# Título de la app
st.title("Mapa por Departamento")

# Menú desplegable para seleccionar departamento
departamento_seleccionado = st.selectbox("Selecciona un Departamento:", departamentos)

# Cargar y mostrar el archivo HTML correspondiente
if departamento_seleccionado:
    archivo_html = f"{departamento_seleccionado}.html"
    try:
        with open(archivo_html, 'r', encoding='utf-8') as f:
            html_content = f.read()
            st.components.v1.html(html_content, height=600, scrolling=True)
    except FileNotFoundError:
        st.error(f"No se encontró el archivo {archivo_html}. Asegúrate de tenerlo en la carpeta correcta.")

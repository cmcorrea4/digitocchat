import streamlit as st
import streamlit.components.v1 as components

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Chatbot App",
        page_icon="💬",
        layout="wide"
    )

    # Título de la aplicación
    st.title("Aplicación con Chatbot Integrado")

    # HTML personalizado que incluye el script del chatbot
    chatbot_html = """
    <div style="height: 600px;">
        <script async
            src="https://agent-b19dea4d7a0319e59496-jmnae.ondigitalocean.app/static/chatbot/widget.js"
            data-agent-id="3cb32dc5-f181-11ef-bf8f-4e013e2ddde4"
            data-chatbot-id="02caM1x3qNq8LsB-oOEQbUaPCNOM9mP_"
            data-name="agent-consinm Chatbot"
            data-primary-color="#031B4E"
            data-secondary-color="#E5E8ED"
            data-button-background-color="#0061EB"
            data-starting-message="Hola!  En que puedo ayudarte?"
            data-logo="/static/chatbot/icons/default-agent.svg">
        </script>
    </div>
    """

    # Contenido principal de la aplicación
    st.markdown("""
    ## Bienvenido a nuestra aplicación
    Esta es una aplicación de demostración que integra un chatbot interactivo.
    Puedes usar el botón del chat que aparece en la esquina inferior derecha.
    """)

    # Insertar el componente HTML con el chatbot
    components.html(chatbot_html, height=600)

    # Contenido adicional de la aplicación
    st.markdown("""
    ### Características:
    - Chatbot interactivo disponible 24/7
    - Interfaz amigable
    - Respuestas instantáneas
    """)

if __name__ == "__main__":
    main()

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
    ####
    st.subheader("💬 Asistente de Voz")
    chat_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Chat Widget</title>
        </head>
        <body>
            <div style="width: 50%; height: 50px;">
                <elevenlabs-convai agent-id="gMh8bGtmxS5OxxPwDuKT"></elevenlabs-convai>
            </div>
            <script src="https://elevenlabs.io/convai-widget/index.js" async></script>
        </body>
        </html>
    """
    st.components.v1.html(chat_html, height=150, scrolling=False)
    st.markdown("---")
    ##

    
    
    # HTML personalizado que incluye el script del chatbot
    chatbot_html = """
    <div style="height: 500px;">
        <script async
            src="https://agent-b19dea4d7a0319e59496-jmnae.ondigitalocean.app/static/chatbot/widget.js"
            data-agent-id="3cb32dc5-f181-11ef-bf8f-4e013e2ddde4"
            data-chatbot-id="02caM1x3qNq8LsB-oOEQbUaPCNOM9mP_"
            data-name="agent-consinm Chatbot"
            data-primary-color="#4A90E2"
            data-secondary-color="#F5F8FA"
            data-button-background-color="#64B5F6"
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
    components.html(chatbot_html, height=500)

    # Contenido adicional de la aplicación
    st.markdown("""
    ### Características:
    - Chatbot interactivo disponible 24/7
    - Interfaz amigable
    - Respuestas instantáneas
    """)


if __name__ == "__main__":
    main()

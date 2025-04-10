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
    st.title("Asistentes de voz y texto")
    ####
    st.subheader("💬 Asistente de Voz")
    st.markdown("""
    ## TEXTO
    Interactua a través de la voz con el asistente.
    """)
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

    st.subheader("💬 Asistente de texto")
    
    # HTML personalizado que incluye el script del chatbot
    chatbot_html = """
    <div style="height: 100px;">
        <script async
          src="https://agent-3f4373bb9b9e2521b014-cd9qj.ondigitalocean.app/static/chatbot/widget.js"
          data-agent-id="de703369-fcf2-11ef-bf8f-4e013e2ddde4"
          data-chatbot-id="M1iBgnKnoSo7U1LS4gvPlJbUb5VWTaWG"
          data-name="agent-sensores Chatbot"
          data-primary-color="#031B4E"
          data-secondary-color="#E5E8ED"
          data-button-background-color="#0061EB"
          data-starting-message="Hola soy Electra, la asisten Digital de SUME EnergyC, en que puedo ayudarte?"
          data-logo="/static/chatbot/icons/default-agent.svg">
        </script>
    </div>
    """

    # Contenido principal de la aplicación
    st.markdown("""
    ## TEXTO
    Interactua de forma textual con el asistente.
    """)

    # Insertar el componente HTML con el chatbot
    components.html(chatbot_html, height=200)

    # Contenido adicional de la aplicación
    st.markdown("""
    ### Características:
    - Chatbot interactivo disponible 24/7
    - Interfaz amigable
    - Respuestas instantáneas
    """)


if __name__ == "__main__":
    main()

import streamlit as st
import streamlit.components.v1 as components

def set_page_style():
    st.markdown("""
        <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .main {
            padding: 1rem;
        }
        .stTitle {
            font-size: 2.5rem !important;
            padding-bottom: 2rem;
            text-align: center;
        }
        .stMarkdown {
            padding: 0.5rem 0;
        }
        div[data-testid="stHorizontalBlock"] {
            padding: 0.5rem 0;
            gap: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="CI - Asistente Virtual",
        page_icon="💬",
        layout="wide"
    )
    
    # Aplicar estilos personalizados
    set_page_style()
    
    # Layout principal
    st.title("CI - Asistente Virtual")
    
    # Crear dos columnas para el contenido principal
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div style='background-color: #f8f9fa; padding: 2rem; border-radius: 10px;'>
            <h2 style='margin-bottom: 1rem;'>Bienvenido a CI</h2>
            <p style='font-size: 1.1rem; color: #333;'>
                Consulta nuestro catálogo de productos y precios de manera fácil y rápida.
                Utiliza nuestros asistentes virtuales para obtener ayuda inmediata.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Asistente de voz con estilo mejorado
        st.subheader("💬 Asistente de Voz")
        chat_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <style>
                    .voice-assistant {
                        background-color: white;
                        padding: 1rem;
                        border-radius: 8px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    }
                </style>
            </head>
            <body>
                <div class="voice-assistant">
                    <elevenlabs-convai agent-id="gMh8bGtmxS5OxxPwDuKT"></elevenlabs-convai>
                </div>
                <script src="https://elevenlabs.io/convai-widget/index.js" async></script>
            </body>
            </html>
        """
        st.components.v1.html(chat_html, height=150, scrolling=False)
    
    with col2:
        st.markdown("""
        <div style='background-color: white; padding: 1.5rem; border-radius: 10px; border: 1px solid #e0e0e0;'>
            <h3 style='margin-bottom: 1rem;'>Servicios Disponibles</h3>
            <ul style='list-style-type: none; padding-left: 0;'>
                <li style='margin-bottom: 0.5rem;'>✓ Consulta de precios en tiempo real</li>
                <li style='margin-bottom: 0.5rem;'>✓ Catálogo de productos actualizado</li>
                <li style='margin-bottom: 0.5rem;'>✓ Asistencia virtual 24/7</li>
                <li style='margin-bottom: 0.5rem;'>✓ Soporte técnico especializado</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Chatbot integrado con altura ajustada
    chatbot_html = """
    <div style="height: 500px;">
        <script async
            src="https://agent-b19dea4d7a0319e59496-jmnae.ondigitalocean.app/static/chatbot/widget.js"
            data-agent-id="3cb32dc5-f181-11ef-bf8f-4e013e2ddde4"
            data-chatbot-id="02caM1x3qNq8LsB-oOEQbUaPCNOM9mP_"
            data-name="CI - Asistente Virtual"
            data-primary-color="#4A90E2"
            data-secondary-color="#F5F8FA"
            data-button-background-color="#64B5F6"
            data-starting-message="¡Hola! ¿En qué puedo ayudarte con nuestros productos?"
            data-logo="/static/chatbot/icons/default-agent.svg">
        </script>
    </div>
    """
    # Insertar el chatbot con altura adecuada
    components.html(chatbot_html, height=500)

    # Footer simple
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #666; font-size: 0.9rem;'>
            © 2024 CI - Todos los derechos reservados
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

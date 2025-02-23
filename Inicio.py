import streamlit as st
import streamlit.components.v1 as components

def set_custom_style():
    st.markdown("""
        <style>
        .main {
            padding: 0rem 1rem;
        }
        .stTitle {
            font-size: 2rem !important;
            padding-bottom: 1rem;
        }
        .stMarkdown {
            padding: 0 !important;
        }
        .row-widget {
            padding: 0.5rem 0;
        }
        .css-1d391kg {
            padding: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

def create_sidebar():
    with st.sidebar:
        st.image("https://via.placeholder.com/150x80?text=CI+Logo", width=150)
        st.markdown("### Navegación")
        st.markdown("- [Productos](#productos)")
        st.markdown("- [Precios](#precios)")
        st.markdown("- [Contacto](#contacto)")
        st.markdown("---")
        st.markdown("### Horario de Atención")
        st.markdown("Lunes a Viernes: 9:00 - 18:00")
        st.markdown("Sábados: 9:00 - 13:00")

def main():
    st.set_page_config(
        page_title="CI - Catálogo de Productos",
        page_icon="🏢",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    set_custom_style()
    create_sidebar()

    # Contenedor principal
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("Catálogo de Productos CI")
        st.markdown("""
        <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 5px;'>
            Bienvenido al catálogo digital de CI. Aquí encontrarás:
            
            ✓ Precios actualizados
            ✓ Especificaciones técnicas
            ✓ Disponibilidad en tiempo real
            
            Utiliza nuestros asistentes virtuales para una atención personalizada.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.subheader("💬 Asistente de Voz")
        chat_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Chat Widget</title>
            </head>
            <body>
                <div style="width: 100%; height: 50px;">
                    <elevenlabs-convai agent-id="gMh8bGtmxS5OxxPwDuKT"></elevenlabs-convai>
                </div>
                <script src="https://elevenlabs.io/convai-widget/index.js" async></script>
            </body>
            </html>
        """
        st.components.v1.html(chat_html, height=100, scrolling=False)

    # Sección de productos
    st.markdown("---")
    st.header("Productos Destacados")
    
    # Grid de productos
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style='background-color: white; padding: 1rem; border-radius: 5px; border: 1px solid #e0e0e0;'>
            <h3>Categoría 1</h3>
            <p>Descripción breve de los productos en esta categoría.</p>
            <button style='background-color: #4A90E2; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px;'>
                Ver más
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: white; padding: 1rem; border-radius: 5px; border: 1px solid #e0e0e0;'>
            <h3>Categoría 2</h3>
            <p>Descripción breve de los productos en esta categoría.</p>
            <button style='background-color: #4A90E2; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px;'>
                Ver más
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background-color: white; padding: 1rem; border-radius: 5px; border: 1px solid #e0e0e0;'>
            <h3>Categoría 3</h3>
            <p>Descripción breve de los productos en esta categoría.</p>
            <button style='background-color: #4A90E2; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px;'>
                Ver más
            </button>
        </div>
        """, unsafe_allow_html=True)

    # Chatbot
    chatbot_html = """
    <div style="height: 0;">
        <script async
            src="https://agent-b19dea4d7a0319e59496-jmnae.ondigitalocean.app/static/chatbot/widget.js"
            data-agent-id="3cb32dc5-f181-11ef-bf8f-4e013e2ddde4"
            data-chatbot-id="02caM1x3qNq8LsB-oOEQbUaPCNOM9mP_"
            data-name="CI Asistente Virtual"
            data-primary-color="#4A90E2"
            data-secondary-color="#F5F8FA"
            data-button-background-color="#64B5F6"
            data-starting-message="¡Hola! Soy el asistente virtual de CI. ¿En qué puedo ayudarte con nuestros productos?"
            data-logo="/static/chatbot/icons/default-agent.svg">
        </script>
    </div>
    """
    components.html(chatbot_html, height=0)

    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Contacto")
        st.markdown("📞 +XX XXX XXX XXX")
        st.markdown("📧 info@ci.com")
    
    with col2:
        st.markdown("### Ubicación")
        st.markdown("🏢 Dirección de la empresa")
        st.markdown("📍 Ciudad, País")
    
    with col3:
        st.markdown("### Síguenos")
        st.markdown("📱 Redes Sociales")

if __name__ == "__main__":
    main()

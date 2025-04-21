import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import base64
from PIL import Image
import io

def get_base64_of_bin_file(bin_file):
    """
    Function to convert binary file to base64 encoding
    """
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background_image(image_file):
    """
    Function to set background image
    """
    bin_str = get_base64_of_bin_file(image_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def add_logo():
    """
    Function to add logo in the sidebar
    """
    st.sidebar.image("logo_sume2.png", width=200)

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Asistentes Digitales SUME",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Añadir logo en la navegación superior
    logo_html = '''
    <div style="display: flex; align-items: center; margin-bottom: 1rem;">
        <img src="data:image/png;base64,{}" style="width: 120px; margin-right: 10px;">
        <h1 style="color: #031B4E; margin: 0;">Asistentes Digitales SUME</h1>
    </div>
    '''
    
    # Si tienes el logo como archivo:
    with open("logo_sume2.png", "rb") as img_file:
        img_bytes = base64.b64encode(img_file.read()).decode()
        st.markdown(logo_html.format(img_bytes), unsafe_allow_html=True)
    
    # Alternativamente, puedes comentar las líneas anteriores y usar esto:
    # st.title("Asistentes Digitales SUME")
    
    # Aplicar CSS personalizado para mejorar la apariencia
    st.markdown("""
    <style>
    /* Colores corporativos */
    :root {
        --primary: #EB6600;
        --secondary: #031B4E;
        --background: #ffffff;
        --text: #333333;
    }
    
    /* Estilos generales */
    .stApp {
        background-color: var(--background);
    }
    
    h1, h2, h3 {
        color: var(--secondary);
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Tarjetas para cada asistente */
    .assistant-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border-left: 5px solid var(--primary);
    }
    
    /* Iconos grandes */
    .icon-large {
        font-size: 2.5rem;
        color: var(--primary);
        margin-bottom: 10px;
    }
    
    /* Menú de navegación */
    .nav-link {
        border-radius: 5px;
        padding: 10px 15px;
        margin: 5px 0;
        background-color: #f8f9fa;
        transition: background-color 0.3s;
    }
    
    .nav-link:hover {
        background-color: var(--primary);
        color: white;
    }
    
    .nav-link.active {
        background-color: var(--primary);
        color: white;
    }
    
    /* Separador con gradiente */
    .gradient-divider {
        height: 3px;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        margin: 20px 0;
        border-radius: 3px;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .assistant-card {
            padding: 15px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Navegación con iconos
    selected = option_menu(
        menu_title=None,
        options=["Inicio", "Asistente de Voz", "Asistente de Energía", "Asistente Textil", "Acerca de"],
        icons=["house", "mic", "lightning", "layers", "info-circle"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f9fa"},
            "icon": {"color": "#EB6600", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#EB6600"},
        }
    )
    
    # Página de inicio
    if selected == "Inicio":
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div class="assistant-card">
                <h2>Bienvenido a los Asistentes Digitales SUME</h2>
                <p>Nuestros asistentes digitales están diseñados para facilitar su interacción con los servicios de SUME Energy. 
                Elija el tipo de asistente que necesita utilizando la barra de navegación superior.</p>
                
                <div class="gradient-divider"></div>
                
                <h3>Nuestros Asistentes:</h3>
                <ul>
                    <li><strong>Asistente de Voz</strong> - Interactúe mediante comandos de voz</li>
                    <li><strong>Asistente de Energía</strong> - Consulte información sobre consumo y eficiencia energética</li>
                    <li><strong>Asistente Textil</strong> - Obtenga asistencia relacionada con nuestros productos textiles</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.image("logo_sume2.png", width=300)
    
    # Asistente de Voz
    elif selected == "Asistente de Voz":
        st.markdown("""
        <div class="assistant-card">
            <div style="display: flex; align-items: center;">
                <i class="material-icons icon-large">mic</i>
                <h2 style="margin-left: 15px;">Asistente de Voz</h2>
            </div>
            <p>Interactúa a través de la voz con nuestro asistente inteligente.</p>
        </div>
        """, unsafe_allow_html=True)
        
        chat_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Chat Widget</title>
                <style>
                    .chat-container {
                        border-radius: 10px;
                        background-color: #f8f9fa;
                        padding: 20px;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    }
                </style>
            </head>
            <body>
                <div class="chat-container">
                    <elevenlabs-convai agent-id="gMh8bGtmxS5OxxPwDuKT"></elevenlabs-convai>
                </div>
                <script src="https://elevenlabs.io/convai-widget/index.js" async></script>
            </body>
            </html>
        """
        st.components.v1.html(chat_html, height=500, scrolling=False)
    
    # Asistente de Energía
    elif selected == "Asistente de Energía":
        st.markdown("""
        <div class="assistant-card">
            <div style="display: flex; align-items: center;">
                <i class="material-icons icon-large">flash_on</i>
                <h2 style="margin-left: 15px;">Asistente de Energía</h2>
            </div>
            <p>Consulta información sobre consumo energético, eficiencia y recomendaciones personalizadas.</p>
        </div>
        """, unsafe_allow_html=True)
        
        chatbot_html = """
        <div class="chat-container" style="border-radius: 10px; background-color: #f8f9fa; padding: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <script async
              src="https://agent-3f4373bb9b9e2521b014-cd9qj.ondigitalocean.app/static/chatbot/widget.js"
              data-agent-id="de703369-fcf2-11ef-bf8f-4e013e2ddde4"
              data-chatbot-id="M1iBgnKnoSo7U1LS4gvPlJbUb5VWTaWG"
              data-name="Electra - Asistente de Energía"
              data-primary-color="#EB6600"
              data-secondary-color="#E5E8ED"
              data-button-background-color="#EB6600"
              data-starting-message="Hola soy Electra, la asistente Digital de SUME EnergyC, ¿en qué puedo ayudarte?"
              data-logo="/static/chatbot/icons/default-agent.svg">
            </script>
        </div>
        """
        components.html(chatbot_html, height=600)
    
    # Asistente Textil
    elif selected == "Asistente Textil":
        st.markdown("""
        <div class="assistant-card">
            <div style="display: flex; align-items: center;">
                <i class="material-icons icon-large">layers</i>
                <h2 style="margin-left: 15px;">Asistente Textil</h2>
            </div>
            <p>Resuelve tus dudas sobre nuestros productos textiles y recomendaciones personalizadas.</p>
        </div>
        """, unsafe_allow_html=True)
        
        chatbot2_html = """
        <div class="chat-container" style="border-radius: 10px; background-color: #f8f9fa; padding: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <script async
              src="https://uq726hao4xro7jumqyhtswwr.agents.do-ai.run/static/chatbot/widget.js"
              data-agent-id="7b5424b4-04e6-11f0-bf8f-4e013e2ddde4"
              data-chatbot-id="w2nmpPtU6h_qGYKXdZ1-hSmvAlRhkzKQ"
              data-name="Asistente Textil SUME"
              data-primary-color="#031B4E"
              data-secondary-color="#E5E8ED"
              data-button-background-color="#0061EB"
              data-starting-message="¡Hola! ¿En qué puedo asistirte con nuestros productos textiles?"
              data-logo="/static/chatbot/icons/default-agent.svg">
            </script>
        </div>
        """
        components.html(chatbot2_html, height=600)
    
    # Acerca de
    elif selected == "Acerca de":
        st.markdown("""
        <div class="assistant-card">
            <h2>Acerca de SUME Energy</h2>
            <p>SUME Energy es una empresa comprometida con la innovación y la eficiencia energética.
            Nuestros asistentes digitales están diseñados para facilitar el acceso a nuestros servicios
            y proporcionar una experiencia de usuario excepcional.</p>
            
            <div class="gradient-divider"></div>
            
            <h3>Contacto</h3>
            <p>Para más información, contáctenos a través de:</p>
            <ul>
                <li>Email: info@sume-energy.com</li>
                <li>Teléfono: +123 456 7890</li>
                <li>Dirección: Calle Principal 123, Ciudad</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.image("logo_sume.png", width=200)

    # Aplicar material design
    material_icons = """
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    """
    st.markdown(material_icons, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="position: fixed; bottom: 0; width: 100%; background-color: #f8f9fa; padding: 10px; text-align: center; border-top: 1px solid #ddd;">
        <p style="margin: 0; font-size: 14px;">© 2025 SUME Energy - Todos los derechos reservados</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Simulação de Evacuação", layout="wide")

# Barra de navegação horizontal
selected = option_menu(
    menu_title=None,  # sem título principal
    options=["Menu", "Mapas", "Parâmetros", "Resultados", "Documentação"],
    icons=["house", "map", "sliders", "bar-chart", "book"],  # ícones do Bootstrap
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Conteúdo de cada página
if selected == "Menu":
    st.title("Simulação de Evacuação de Ambientes")
    st.write("""
    Simule evacuações e avalie a eficiência de diferentes quantidades e posições de saídas de emergência.  
    Uma ferramenta prática para segurança e planejamento. Inicie sua simulação agora!
    """)
    st.image("1.jpg", width=400)  # imagem da sua tela inicial

elif selected == "Mapas":
    st.title("Mapas")
    st.write("Aqui será carregado o ambiente e mapa para a simulação.")

elif selected == "Parâmetros":
    st.title("Parâmetros")
    st.write("Configuração de parâmetros da simulação.")

elif selected == "Resultados":
    st.title("Resultados")
    st.write("Visualização dos resultados da simulação.")

elif selected == "Documentação":
    st.title("Documentação")
    st.write("Explicação de como o sistema funciona e instruções de uso.")

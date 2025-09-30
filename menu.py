import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Projeto com Streamlit", layout="wide")

# Estado compartilhado (garante que session_state tenha as chaves que vamos usar)
if "pagina" not in st.session_state:
    st.session_state.pagina = "Menu"

# Barra de navegação
selected = option_menu(
    menu_title=None,
    options=["Menu", "Mapas", "Parâmetros", "Resultados", "Documentação"],
    icons=["house", "map", "sliders", "bar-chart", "book"],
    default_index=0,
    orientation="horizontal",
)

# Salva a página selecionada
st.session_state.pagina = selected

# Renderiza cada aba
if selected == "Menu":
    st.title("📌 Página Inicial")
    st.write("Bem-vindo ao sistema. Use o menu acima para navegar.")

elif selected == "Mapas":
    # Importa a função da página Mapas
    import mapas
    mapas.mostrar()

elif selected == "Parâmetros":
    st.title("⚙️ Parâmetros")
    st.write("Aqui você pode ajustar parâmetros.")

elif selected == "Resultados":
    st.title("📊 Resultados")
    st.write("Aqui serão exibidos os resultados.")

elif selected == "Documentação":
    st.title("📖 Documentação")
    st.write("Aqui entra a documentação do projeto.")

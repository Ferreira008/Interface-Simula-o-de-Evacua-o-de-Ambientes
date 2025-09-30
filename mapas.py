import streamlit as st

def mostrar():
    st.title("🗺️ Mapas disponíveis")

    # Layout em grid
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://via.placeholder.com/300x200", caption="Mapa 1")
    with col2:
        st.image("https://via.placeholder.com/300x200", caption="Mapa 2")
    with col3:
        st.image("https://via.placeholder.com/300x200", caption="Mapa 3")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://via.placeholder.com/300x200", caption="Mapa 4")
    with col5:
        st.image("https://via.placeholder.com/300x200", caption="Mapa 5")
    with col6:
        st.image("https://via.placeholder.com/300x200", caption="Mapa 6")

    col7, col8, _ = st.columns(3)
    with col7:
        st.image("https://via.placeholder.com/300x200", caption="Mapa 7")
    with col8:
        st.button("➕ Adicionar novo mapa")

import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Simulação de Evacuação", layout="wide")

# ---- Custom CSS to match the provided mock ----
st.markdown(
    """
    <style>
    /* Base layout */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
        background: #ffffff !important;
        color: #111111 !important;
    }

    /* Remove default Streamlit padding at the top */
    .block-container { padding-top: 1.2rem; padding-bottom: 2rem; }

    /* Top navigation bar */
    .top-nav {
        display: flex;
        gap: 48px;
        align-items: center;
        font-size: 22px;
        margin-bottom: 32px;
        user-select: none;
    }
    .top-nav .active { font-weight: 800; color: #111111; }
    .top-nav .inactive { color: #9b9b9b; font-weight: 700; }

    /* Big title style */
    .hero-title { font-size: clamp(36px, 5vw, 64px); line-height: 1.1; font-weight: 800; color: #111111; margin: 18px 0 12px 0; }

    .lead { font-size: clamp(16px, 1.4vw, 22px); color: #111111; }

    /* Footer logos bottom-right */
    .brand-footer {
        position: fixed; bottom: 24px; right: 24px;
        display: flex; gap: 28px; align-items: center;
        opacity: 0.95;
    }
    .brand-footer img { height: 42px; }

    /* Hide Streamlit default header/footer */
    header[data-testid="stHeader"] { display: none; }
    footer { visibility: hidden; }

    /* Ensure main and sidebar backgrounds remain white regardless of theme */
    [data-testid="stAppViewContainer"] > .main { background: #ffffff !important; }
    [data-testid="stSidebar"] { background: #ffffff !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- Top Menu (text only) ----
st.markdown(
    """
    <div class="top-nav">
      <span class="active">Menu</span>
      <span class="inactive">Mapas</span>
      <span class="inactive">Parâmetros</span>
      <span class="inactive">Resultados</span>
      <span class="inactive">Documentação</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---- Body: two columns ----
col_left, col_right = st.columns([0.58, 0.42])

with col_left:
    st.markdown(
        "<div class='hero-title'>Simulação de Evacuação de Ambientes</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="lead">
        Simule evacuações e avalie a eficiência de diferentes quantidades e posições de saídas de emergência. 
        Uma ferramenta prática para segurança e planejamento. Inicie sua simulação agora!
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_right:
    runner_path = Path("assets/runner_exit.svg")
    if runner_path.exists():
        st.image(str(runner_path), use_container_width=True)

# ---- Bottom-right logos ----
assets = Path("assets")
if (assets / "if_logo.svg").exists() and (assets / "cefet_logo.svg").exists():
    st.markdown(
        f"""
        <div class="brand-footer">
            <img src="{(assets / 'if_logo.svg').as_posix()}" alt="IF" />
            <img src="{(assets / 'cefet_logo.svg').as_posix()}" alt="CEFET-MG" />
        </div>
        """,
        unsafe_allow_html=True,
    )
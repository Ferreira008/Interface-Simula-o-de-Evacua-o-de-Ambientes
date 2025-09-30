import streamlit as st


def inject_base_styles() -> None:

    st.markdown(
        """
        <style>
        /* Global resets and typography */
        html, body, [class^="css"], .stApp {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", Arial, sans-serif;
            color: #111111;
        }

        /* Hide Streamlit default chrome for a clean look */
        #MainMenu, footer {visibility: hidden;}

        /* Header navigation */
        .app-nav {
            display: flex;
            gap: 40px;
            align-items: center;
            padding: 16px 0 8px 0;
        }
        .app-nav .nav-item { 
            font-size: 22px;
            line-height: 1;
            color: #8c8c8c; /* inactive gray */
            font-weight: 700; /* keep strong visual weight like the mock */
        }
        .app-nav .nav-item.active { 
            color: #000000; /* active black */
        }

        /* Main hero section */
        .hero-title {
            font-size: clamp(36px, 5.5vw, 72px);
            font-weight: 800;
            margin: 32px 0 24px 0;
        }
        .hero-text {
            font-size: clamp(16px, 1.4vw, 22px);
            line-height: 1.7;
            color: #111111;
        }

        /* Right image composition (runner + exit sign) */
        .figure-wrap {
            position: relative;
            width: 100%;
            aspect-ratio: 1.3 / 1; /* makes space similar to mock */
        }
        .figure-wrap img {
            position: absolute;
            max-width: 100%;
            height: auto;
        }
        .exit-sign {
            right: 0;
            top: 0;
            width: min(75%, 520px);
        }
        .runner {
            right: min(8%, 60px);
            bottom: min(6%, 40px);
            width: min(68%, 470px);
            filter: drop-shadow(0 2px 1px rgba(0,0,0,0.08));
        }

        /* Bottom-right partner logos */
        .brand-footer {
            position: fixed; 
            right: 24px; 
            bottom: 24px; 
            display: flex; 
            align-items: center; 
            gap: 22px;
            z-index: 10;
        }
        .brand-footer img { 
            height: 48px; 
            width: auto; 
        }

        /* Tighten Streamlit container paddings slightly for a centered, airy layout */
        .block-container { 
            padding-top: 12px !important; 
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_navbar() -> None:

    st.markdown(
        """
        <div class="app-nav">
            <span class="nav-item active">Menu</span>
            <span class="nav-item">Mapas</span>
            <span class="nav-item">Parâmetros</span>
            <span class="nav-item">Resultados</span>
            <span class="nav-item">Documentação</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero_section() -> None:

    left_col, right_col = st.columns([7, 5], gap="large")

    with left_col:
        st.markdown(
            """
            <div class="hero-title">Simulação de Evacuação de Ambientes</div>
            <div class="hero-text">
            Simule evacuações e avalie a eficiência de diferentes quantidades e posições de saídas de emergência. 
            Uma ferramenta prática para segurança e planejamento. Inicie sua simulação agora!
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right_col:
        # Compose two images with overlap to resemble the reference
        st.markdown(
            """
            <div class="figure-wrap">
                <img class="exit-sign" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/ISO_7010_E001.svg/640px-ISO_7010_E001.svg.png" alt="Exit sign">
                <img class="runner" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Running_icon_-_Noun_Project_5880.svg/640px-Running_icon_-_Noun_Project_5880.svg.png" alt="Running silhouette">
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_brand_footer() -> None:

    st.markdown(
        """
        <div class="brand-footer">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Marca_IFET.svg/200px-Marca_IFET.svg.png" alt="Logo IF" />
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Logo_CEFET-MG.png/300px-Logo_CEFET-MG.png" alt="Logo CEFET-MG" />
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:

    st.set_page_config(
        page_title="Simulação de Evacuação de Ambientes",
        layout="wide",
        page_icon="✅",
    )

    inject_base_styles()
    render_navbar()
    render_hero_section()
    render_brand_footer()


if __name__ == "__main__":
    main()


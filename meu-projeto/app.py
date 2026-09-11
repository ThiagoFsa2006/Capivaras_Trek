import streamlit as st
from PIL import Image
import os

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================

st.set_page_config(
    page_title="Capivaras Trek",
    layout="wide"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

/* Remove elementos nativos do Streamlit */

[data-testid="stHeader"]{
    display:none !important;
}

[data-testid="stToolbar"]{
    display:none !important;
}

[data-testid="stDecoration"]{
    display:none !important;
}

#MainMenu{
    visibility:hidden !important;
}

footer{
    visibility:hidden !important;
}

/* Layout */

.block-container{
    padding-top: 1rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: 100% !important;
}

/* Fundo */

.stApp{
    background: linear-gradient(
        180deg,
        #97a97c 0%,
        #ffffff 100%
    );
}

/* Logo */

.logo-titulo{
    font-size: 34px;
    font-weight: 800;
    color: #244029;
    margin-top: 12px;
}

/* Botões menu */

.stButton > button{
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;

    color: #244029 !important;
    font-weight: 700 !important;

    transition: all .3s ease;
}

.stButton > button:hover{
    color: #6b8e23 !important;
    transform: translateY(-2px);
}

/* Remove bordas ao clicar */

.stButton > button:focus{
    border: none !important;
    box-shadow: none !important;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

col_logo, c1, c2, c3, c4, c5, c6 = st.columns(
    [4, 1, 1, 1, 1, 1, 1]
)

with col_logo:

    img_col, txt_col = st.columns([1, 5])

    with img_col:

        if os.path.exists("logo.png"):
            logo = Image.open("logo.png")
            st.image(logo, width=85)
        else:
            st.markdown(
                "<h1 style='margin-top:10px;'>🦫</h1>",
                unsafe_allow_html=True
            )

    with txt_col:
        st.markdown(
            """
            <div class="logo-titulo">
                Capivaras Trek
            </div>
            """,
            unsafe_allow_html=True
        )

with c1:
    st.button("Home", use_container_width=True)

with c2:
    st.button("Trilhas", use_container_width=True)

with c3:
    st.button("Acervo", use_container_width=True)

with c4:
    st.button("Calendário", use_container_width=True)

with c5:
    st.button("Blog", use_container_width=True)

with c6:
    st.button("Contato", use_container_width=True)

# ==================================================
# ESPAÇAMENTO
# ==================================================

st.write("")
st.write("")

# ==================================================
# CONTEÚDO TEMPORÁRIO
# ==================================================

st.empty()

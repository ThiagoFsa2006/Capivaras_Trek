import streamlit as st
import os
from PIL import Image

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================

st.set_page_config(
    page_title="Capivaras Trek",
    layout="wide"
)

# ==================================================
# CSS GLOBAL
# ==================================================

st.markdown("""
<style>

/* Remove elementos do Streamlit */
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

/* Remove espaço superior */
.block-container{
    padding-top:0rem !important;
    padding-left:1rem !important;
    padding-right:1rem !important;
    max-width:100% !important;
}

/* Fundo */
.stApp{
    background: linear-gradient(
        180deg,
        #97a97c 0%,
        #FFFFFF 100%
    );
}

/* Logo */
.logo{
    font-size:36px;
    font-weight:800;
    color:#244029;
    padding-top:10px;
}

/* ==================================================
   BOTÕES MENU - FONTE 18px
   ================================================== */

div[data-testid="stButton"] button{
    width:100% !important;
    background:transparent !important;
    border:none !important;
    box-shadow:none !important;
    min-height:80px !important;
}

/* força o tamanho de todos os elementos internos */
div[data-testid="stButton"] button,
div[data-testid="stButton"] button *,
div[data-testid="stButton"] button span,
div[data-testid="stButton"] button p{
    font-size:14px !important;
    font-weight:700 !important;
    color:#244029 !important;
}

div[data-testid="stButton"] button:hover{
    background:transparent !important;
}

div[data-testid="stButton"] button:hover *{
    color:#6b8e23 !important;
}

div[data-testid="stButton"] button:focus{
    border:none !important;
    box-shadow:none !important;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

col_logo, c1, c2, c3, c4, c5 = st.columns(
    [4, 1, 1, 1, 1, 1]
)

with col_logo:

    col_img, col_txt = st.columns([0.65, 4])

    logo_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "logo.png"
    )

    with col_img:
        if os.path.exists(logo_path):
            st.image(logo_path, width=80)
        else:
            st.error(f"Logo não encontrada: {logo_path}")

    with col_txt:
        st.markdown(
            """
            <div class="logo">
                Capivaras Trek
            </div>
            """,
            unsafe_allow_html=True
        )

with c1:
    st.button("Home")

with c2:
    st.button("Trilhas")

with c3:
    st.button("Acervo")

with c4:
    st.button("Calendário")

with c5:
    st.button("Contato")
from PIL import Image

# ==================================================
# BANNER
# ==================================================

banner_path = os.path.join(
    os.path.dirname(__file__),
    "assets",
    "banner_home.jpg"
)

if os.path.exists(banner_path):

    img = Image.open(banner_path)

    # gira para a esquerda
    img = img.rotate(270)

    largura, altura = img.size

    # banner panorâmico
    altura_banner = int(largura * 0.30)

    top = (altura - altura_banner) // 2
    bottom = top + altura_banner

    img = img.crop((0, top, largura, bottom))

    st.image(
        img,
        use_container_width=True
    )
# ==================================================
# CONTEÚDO TEMPORÁRIO
# ==================================================

st.write("")
st.write("")
st.write("")

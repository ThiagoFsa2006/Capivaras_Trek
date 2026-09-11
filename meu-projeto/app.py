import streamlit as st
import os
import base64

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================

st.set_page_config(
    page_title="Capivaras Trek",
    layout="wide"
)

# ==================================================
# FUNÇÃO PARA CARREGAR A LOGO
# ==================================================

def get_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

logo_path = os.path.join(
    os.path.dirname(__file__),
    "assets",
    "logo.png"
)

logo_base64 = get_base64(logo_path)

# ==================================================
# CSS GLOBAL
# ==================================================

st.markdown("""
<style>

/* Remove elementos padrão do Streamlit */

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

/* Remove espaçamentos padrão */

.block-container{
    padding-top:0rem !important;
    padding-left:1rem !important;
    padding-right:1rem !important;
    max-width:100% !important;
}

/* Fundo principal */

.stApp{
    background: linear-gradient(
        180deg,
        #97a97c 0%,
        #FFFFFF 100%
    );
}

/* Logo */

.logo-area{
    display:flex;
    align-items:center;
    gap:8px;
}

.logo-area img{
    height:70px;
}

.logo-text{
    font-size:32px;
    font-weight:800;
    color:#244029;
}

/* Botões da navbar */

.stButton button{
    width:100%;
    background:transparent;
    border:none;
    color:#244029;
    font-weight:700;
    transition:0.3s;
}

.stButton button:hover{
    color:#6b8e23;
    transform:translateY(-2px);
}

.stButton button:focus{
    box-shadow:none !important;
    border:none !important;
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
    st.markdown(
        f"""
        <div class="logo-area">
            data:image/png;base64,{logo_base64}
            <div class="logo-text">
                Capivaras Trek
            </div>
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
    st.button("Blog")

with c6:
    st.button("Contato")

# ==================================================
# CONTEÚDO TEMPORÁRIO
# ==================================================

st.write("")
st.write("")
st.write("")

st.markdown(
    """
    <h1 style='color:#244029'>
        Bem-vindo ao Capivaras Trek 🥾
    </h1>
    """,
    unsafe_allow_html=True
)

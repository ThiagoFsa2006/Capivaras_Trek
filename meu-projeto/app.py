import streamlit as st

# --------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------------

st.set_page_config(
    page_title="Capivaras Trek",
    layout="wide"
)

# --------------------------------------------------
# CSS GLOBAL
# --------------------------------------------------

st.markdown("""
<style>

/* REMOVE ELEMENTOS NATIVOS DO STREAMLIT */

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

/* REMOVE BARRA DO COMMUNITY CLOUD */

div[data-testid="stStatusWidget"]{
    display:none !important;
}

button[kind="header"]{
    display:none !important;
}

.stAppDeployButton{
    display:none !important;
}

/* AJUSTE GERAL */

.block-container{
    padding-top:0rem !important;
    padding-left:0rem !important;
    padding-right:0rem !important;
    max-width:100% !important;
}

/* FUNDO ORIGINAL */

.stApp{
    background: linear-gradient(
        180deg,
        #97a97c 0%,
        #FFFFFF 100%
    );
}

/* HEADER */

.capy-header{
    position:fixed;
    top:15px;
    left:20px;
    right:20px;

    height:80px;

    display:flex;
    align-items:center;
    justify-content:space-between;

    padding:0 40px;

    background:rgba(255,255,255,0.18);

    backdrop-filter:blur(20px);
    -webkit-backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,0.25);

    border-radius:22px;

    box-shadow:0 8px 25px rgba(0,0,0,0.12);

    z-index:9999;
}

/* LOGO */

.capy-logo{
    font-size:30px;
    font-weight:800;
    color:#243b21;
}

/* MENU */

.capy-menu{
    display:flex;
    gap:30px;
}

.capy-menu a{
    text-decoration:none;
    color:#2d4f2b;
    font-size:16px;
    font-weight:600;

    transition:all .3s ease;
}

.capy-menu a:hover{
    color:#6b8e23;
    transform:translateY(-2px);
}

/* ESPAÇO PARA O HEADER FIXO */

.page-spacing{
    height:110px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="capy-header">

    <div class="capy-logo">
        🦫 Capivaras Trek
    </div>

    <div class="capy-menu">
        #Home</a>
        #Trilhas</a>
        #Acervo</a>
        #Calendário</a>
        #Blog</a>
        #Contato</a>
    </div>

</div>

<div class="page-spacing"></div>
""", unsafe_allow_html=True)

import streamlit as st

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

/* Fundo original */

.stApp{
    background: linear-gradient(
        180deg,
        #97a97c 0%,
        #FFFFFF 100%
    );
}

/* Header */

.header-box{
    background: rgba(255,255,255,0.18);
    backdrop-filter: blur(15px);

    border:1px solid rgba(255,255,255,0.25);

    border-radius:25px;

    padding:10px 25px;

    margin-top:10px;
    margin-bottom:20px;

    box-shadow:0 10px 25px rgba(0,0,0,0.12);
}

/* Logo */

.logo{
    font-size:32px;
    font-weight:800;
    color:#244029;
}

/* Botões */

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

/* Oculta bordas nos botões */

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
    [4,1,1,1,1,1,1]
)

with col_logo:
    st.markdown(
        '<div class="logo">🦫 Capivaras Trek</div>',
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

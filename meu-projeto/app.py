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

/* Espaçamento da página */

.block-container{
    padding-top: 1rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: 100% !important;
}

/* Fundo original */

.stApp{
    background: linear-gradient(
        180deg,
        #97a97c 0%,
        #FFFFFF 100%
    );
}

/* Logo */

.logo-titulo{
    font-size: 34px;
    font-weight: 800;
    color: #244029;
    padding-top: 12px;
}

/* Botões do menu */

.stButton button{
    width: 100%;
    background: transparent !important;
    border: none !important;
    color: #244029 !important;
    font-weight: 700 !important;
    box-shadow: none !important;
}

.stButton button:hover{
    color: #6b8e23 !important;
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

    img_col, text_col = st.columns([1, 4])

    with img_col:
        st.image("logo.png", width=90)

    with text_col:
        st.markdown(
            '<div class="logo-titulo">Capivaras Trek</div>',
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

st.divider()

# ==================================================
# CONTEÚDO TEMPORÁRIO
# ==================================================

st.write("")
st.write("")
st.write("")

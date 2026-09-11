import streamlit as st

st.set_page_config(page_title="Capivaras Trek", layout="wide")

st.markdown("""
<style>
/* Esconde o cabeçalho nativo */
header[data-testid="stHeader"], div[data-testid="stHeader"] {
    display: none;
}

/* Remove o espaço em branco excessivo no topo da página */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
}

.header-container {
    border: 2px solid #333;
    border-radius: 12px;
    padding: 15px 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: white;
    margin-bottom: 30px;
}

.logo-area h1{
    margin: 0;
    font-size: 36px;
    color: black;
    font-weight: bold;
}

.logo-area p{
    margin: 0;
    font-size: 14px;
    color: #444;
}

.menu{
    display: flex;
    gap: 25px;
}

.menu a{
    text-decoration: none;
    color: black;
    font-size: 16px;
    font-weight: 500;
}

.menu a:hover{
    color: #2e8b57;
}
</style>

<div class="header-container">
    <div class="logo-area">
        <h1>Capivaras Trek</h1>
        <p>Explore a Natureza, Siga as Capivaras</p>
    </div>
    <div class="menu">
        <a href="#home">Home</a>
        <a href="#trilhas">Trilhas</a>
        <a href="#acervo">Acervo</a>
        <a href="#calendario">Calendário</a>
        <a href="#contato">Contato</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("Conteúdo da página...")

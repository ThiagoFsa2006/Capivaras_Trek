import streamlit as st

st.set_page_config(
    page_title="Capivaras Trek",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* Fundo da página */
.stApp {
    background: linear-gradient(
        135deg,
        #3E5831 0%,
        #FFFFFF 100%
    );
}

/* Remove elementos nativos do Streamlit */
header[data-testid="stHeader"] {
    display: none;
}

[data-testid="stToolbar"] {
    display: none;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Remove espaço superior */
.block-container {
    padding-top: 0.2rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    padding-bottom: 0rem !important;
}

/* Header */
.header-container {
    border: 2px solid #333;
    border-radius: 12px;
    padding: 15px 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: rgba(255,255,255,0.92);
    margin-bottom: 30px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
}

/* Logo */
.logo-area h1 {
    margin: 0;
    color: #000;
    font-size: 36px;
    font-weight: 700;
}

.logo-area p {
    margin-top: 5px;
    margin-bottom: 0;
    color: #444;
    font-size: 14px;
}

/* Menu */
.menu {
    display: flex;
    gap: 25px;
}

.menu a {
    text-decoration: none;
    color: #000;
    font-size: 16px;
    font-weight: 600;
    transition: 0.3s;
}

.menu a:hover {
    color: #3E5831;
}

/* Hero */
.hero {
    text-align: center;
    padding: 100px 20px;
    color: white;
}

.hero h2 {
    font-size: 56px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 22px;
}

</style>

<div class="header-container">

    <div class="logo-area">
        <h1>Capivaras Trek</h1>
        <p>Explore a Natureza, Siga as Capivaras</p>
    </div>

    <div class="menu">
        #homeHome</a>
        <arilhasTrilhas</a>
        <acervoAcervo</a>
        <a href="#calendario">Calendário  #contatoContato</a>
    </div>

</div>

<div class="hero">
    <h2>Bem-vindo ao Capivaras Trek</h2>
    <p>Descubra trilhas, aventuras e a natureza de um jeito único.</p>
</div>

""", unsafe_allow_html=True)

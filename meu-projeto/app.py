import streamlit as st

st.set_page_config(page_title="Capivaras Trek", layout="wide")

st.markdown("""
<style>

/* Remove header do Streamlit */
header[data-testid="stHeader"] {
    display: none;
}

/* Remove espaços superiores */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
}

/* Remove margem acima do conteúdo */
div[data-testid="stAppViewContainer"] {
    margin-top: 0px;
}

/* Container principal */
.header-container {
    border: 2px solid #333;
    border-radius: 12px;
    padding: 15px 25px;
    margin-top: 0px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: white;
}

.logo-area h1{
    margin: 0;
    font-size: 36px;
    color: black;
    font-weight: bold;
}

.logo-area p{
    margin-top: 5px;
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
        #homeHome</a>
        #trilhasTrilhas</a>
        #acervoAcervo</a>
        <aalendarioCalendário</a>
        <alogBlog</a>
        <a href="#contato">
    </div>
</div>

""", unsafe_allow_html=True)

st.write("Conteúdo da página...")

import streamlit as st

st.set_page_config(
    page_title="Capivaras Trek",
    layout="wide"
)

st.markdown("""
<style>

.header-container{
    position:fixed;
    top:15px;
    left:20px;
    right:20px;

    height:75px;

    display:flex;
    align-items:center;
    justify-content:space-between;

    padding:0 35px;

    background:rgba(255,255,255,0.20);

    backdrop-filter:blur(12px);
    -webkit-backdrop-filter:blur(12px);

    border-radius:20px;

    box-shadow:0 8px 25px rgba(0,0,0,0.15);

    z-index:9999;
}

.header-menu{
    display:flex;
    gap:30px;
}

.header-menu a{
    text-decoration:none;
    color:#29402a;
    font-size:16px;
    font-weight:600;
}

.header-logo{
    font-size:28px;
    font-weight:800;
    color:#1f3a1f;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-container">

    <div class="header-menu">
        #Home</a>
        #Trilhas</a>
        #Acervo</a>
        #Calendário</a>
        #Blog</a>
        #Contato</a>
    </div>

    <div class="header-logo">
        🦫 Capivaras Trek
    </div>

</div>
""", unsafe_allow_html=True)

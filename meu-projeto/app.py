import streamlit as st

st.set_page_config(page_title="Minha Página", layout="wide")

st.markdown("""
<style>

[data-testid="stHeader"] {
    display: none !important;
}

[data-testid="stToolbar"] {
    display: none !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}

#MainMenu {
    visibility: hidden !important;
}

footer {
    visibility: hidden !important;
}

.block-container {
    padding-top: 0rem !important;
}

.stApp {
    background: linear-gradient(180deg, #97a97c 0%, #FFFFFF 100%);
}

</style>
""", unsafe_allow_html=True)

import streamlit as st

st.set_page_config(
    page_title="Hello World",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="stHeader"] {
    display: none;
}
[data-testid="stToolbar"] {
    display: none;
}
[data-testid="stDecoration"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;">
    <h1 style="color:black;font-size:36px;">
        Hello World
    </h1>
</div>
""", unsafe_allow_html=True)

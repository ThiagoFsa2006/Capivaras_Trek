import streamlit as st

st.set_page_config(page_title="Hello World", layout="wide")

st.markdown(
    """
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    ">
        <h1 style="
            color: black;
            font-size: 36px;
            margin: 0;
        ">
            Hello World
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

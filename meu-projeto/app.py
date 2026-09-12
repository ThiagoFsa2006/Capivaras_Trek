import streamlit as st
import streamlit.components.v1 as components
import os
import base64

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

/* Fundo */
.stApp{
    background: linear-gradient(
        180deg,
        #97a97c 0%,
        #FFFFFF 100%
    );
}

/* Logo */
.logo{
    font-size:36px;
    font-weight:800;
    color:#244029;
    padding-top:10px;
}

/* ==================================================
   BOTÕES MENU
   ================================================== */

div[data-testid="stButton"] button{
    width:100% !important;
    background:transparent !important;
    border:none !important;
    box-shadow:none !important;
    min-height:80px !important;
}

div[data-testid="stButton"] button,
div[data-testid="stButton"] button *,
div[data-testid="stButton"] button span,
div[data-testid="stButton"] button p{
    font-size:14px !important;
    font-weight:700 !important;
    color:#244029 !important;
}

div[data-testid="stButton"] button:hover{
    background:transparent !important;
}

div[data-testid="stButton"] button:hover *{
    color:#6b8e23 !important;
}

div[data-testid="stButton"] button:focus{
    border:none !important;
    box-shadow:none !important;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

col_logo, c1, c2, c3, c4, c5 = st.columns(
    [4, 1, 1, 1, 1, 1]
)

with col_logo:

    col_img, col_txt = st.columns([0.65, 4])

    logo_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "logo.png"
    )

    with col_img:
        if os.path.exists(logo_path):
            st.image(logo_path, width=80)
        else:
            st.error(f"Logo não encontrada: {logo_path}")

    with col_txt:
        st.markdown(
            """
            <div class="logo">
                Capivaras Trek
            </div>
            """,
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
    st.button("Contato")

# ==================================================
# HELPER PARA CARREGAR IMAGEM LOCAL EM BASE64
# ==================================================

def get_image_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        ext = os.path.splitext(file_path)[1].replace(".", "").lower()
        if ext == "jpg":
            ext = "jpeg"
        return f"data:image/{ext};base64,{encoded}"
    return ""

# ==================================================
# CARROSSEL HERO
# ==================================================

def render_hero_carousel():
    assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    
    img1 = get_image_base64(os.path.join(assets_dir, "banner_home.jpg"))
    img2 = get_image_base64(os.path.join(assets_dir, "banner_home1.jpg"))
    img3 = get_image_base64(os.path.join(assets_dir, "banner_home2.jpg"))

    fallback = "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1600"
    img1 = img1 if img1 else fallback
    img2 = img2 if img2 else fallback
    img3 = img3 if img3 else fallback

    carousel_html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
      <meta charset="UTF-8">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
      <style>
        * {{
          box-sizing: border-box;
          margin: 0;
          padding: 0;
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }}

        body {{
          background: transparent;
          padding: 10px 0;
        }}

        .swiper {{
          width: 100%;
          border-radius: 24px;
          overflow: hidden;
          box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }}

        .swiper-slide {{
          position: relative;
          height: 600px;
          background-size: cover;
          display: flex;
          justify-content: center;
          align-items: center;
          color: #ffffff;
        }}

        /* Posicionamento customizado das imagens */
        .slide-1 {{
          background-position: center 40%;
        }}

        .slide-2 {{
          background-position: center 40%;
        }}

        .slide-3 {{
          background-position: center 50%;
        }}

        .swiper-slide::before {{
          content: "";
          position: absolute;
          inset: 0;
          background: rgba(0, 0, 0, 0.35);
          z-index: 1;
        }}

        .hero-title-container {{
          position: relative;
          z-index: 2;
          text-align: center;
          padding: 0 20px;
        }}

        .hero-title {{
          font-size: 52px;
          font-weight: 900;
          letter-spacing: 3px;
          text-transform: uppercase;
          line-height: 1.15;
          color: #ffffff;
          text-shadow: 0 4px 12px rgba(0,0,0,0.6);
        }}

        .swiper-pagination {{
          position: relative !important;
          margin-top: 15px !important;
          bottom: 0 !important;
        }}

        .swiper-pagination-bullet {{
          width: 12px;
          height: 12px;
          background: #244029;
          opacity: 0.4;
        }}

        .swiper-pagination-bullet-active {{
          background: #244029 !important;
          opacity: 1;
          width: 14px;
          height: 14px;
        }}

        .swiper-button-next, .swiper-button-prev {{
          color: #ffffff !important;
          transform: scale(0.6);
          z-index: 10;
        }}
      </style>
    </head>
    <body>

      <div class="swiper mySwiper">
        <div class="swiper-wrapper">

          <!-- SLIDE 1 -->
          <div class="swiper-slide slide-1" style="background-image: url('{img1}');">
            <div class="hero-title-container">
              <h1 class="hero-title">CUME DO TAIPABUÇO</h1>
            </div>
          </div>

          <!-- SLIDE 2 -->
          <div class="swiper-slide slide-2" style="background-image: url('{img2}');">
            <div class="hero-title-container">
              <h1 class="hero-title">CACHOEIRA DA LAPINHA</h1>
            </div>
          </div>

          <!-- SLIDE 3 -->
          <div class="swiper-slide slide-3" style="background-image: url('{img3}');">
            <div class="hero-title-container">
              <h1 class="hero-title">CUME DO ANHANGAVA</h1>
            </div>
          </div>

        </div>

        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
      </div>

      <div class="swiper-pagination"></div>

      <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
      <script>
        var swiper = new Swiper(".mySwiper", {{
          loop: true,
          autoplay: {{
            delay: 6000, /* 7 segundos de duração por slide */
            disableOnInteraction: false,
          }},
          pagination: {{
            el: ".swiper-pagination",
            clickable: true,
          }},
          navigation: {{
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
          }},
        }});
      </script>
    </body>
    </html>
    """
    components.html(carousel_html, height=660)

render_hero_carousel()

# ==================================================
# CONTEÚDO TEMPORÁRIO
# ==================================================

st.write("")
st.write("")
st.write("")

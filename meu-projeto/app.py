import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================

st.set_page_config(
    page_title="Capivaras Trek — Montanhismo & Aventuras",
    page_icon="🏔️",
    layout="wide"
)

# ==================================================
# CSS GLOBAL REFINADO (COM SUPORTE MOBILE)
# ==================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
#MainMenu,
footer {
    display: none !important;
    visibility: hidden !important;
}

.block-container {
    padding-top: 0rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    padding-bottom: 0rem !important;
    max-width: 100% !important;
}

.stApp {
    background: linear-gradient(180deg, #8ba170 0%, #edf1e8 50%, #ffffff 100%);
}

/* ==================================================
   HEADER & NAVBAR
   ================================================== */

.logo-text {
    font-size: 32px;
    font-weight: 900;
    color: #1c3320;
    letter-spacing: -0.5px;
    line-height: 1;
}

div[data-testid="stButton"] button {
    width: 100% !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    min-height: 70px !important;
    border-bottom: 3px solid transparent !important;
    border-radius: 0px !important;
    transition: all 0.25s ease-in-out !important;
}

div[data-testid="stButton"] button p,
div[data-testid="stButton"] button span {
    font-size: 15px !important;
    font-weight: 700 !important;
    color: #1c3320 !important;
    letter-spacing: 0.3px !important;
}

div[data-testid="stButton"] button:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    border-bottom: 3px solid #244029 !important;
}

div[data-testid="stButton"] button:hover p {
    color: #244029 !important;
}

div[data-testid="stButton"] button:focus {
    border: none !important;
    box-shadow: none !important;
}

/* ==================================================
   SEÇÃO QUEM SOMOS & STATS
   ================================================== */

.about-card {
    max-width: 1100px;
    margin: 50px auto 30px auto;
    padding: 50px;
    background: rgba(255, 255, 255, 0.85);
    border-radius: 24px;
    backdrop-filter: blur(12px);
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.6);
}

.about-title {
    font-size: 32px;
    font-weight: 900;
    color: #1c3320;
    text-align: center;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

.about-subtitle-line {
    width: 60px;
    height: 4px;
    background-color: #557242;
    margin: -10px auto 30px auto;
    border-radius: 2px;
}

.about-text {
    font-size: 17px;
    line-height: 1.85;
    color: #38423b;
    text-align: center;
    max-width: 900px;
    margin: 0 auto 18px auto;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 40px;
}

.stat-item {
    background: #ffffff;
    padding: 25px 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    border: 1px solid #eef2eb;
}

.stat-icon {
    font-size: 28px;
    margin-bottom: 8px;
}

.stat-number {
    font-size: 26px;
    font-weight: 800;
    color: #244029;
}

.stat-label {
    font-size: 14px;
    color: #666;
    font-weight: 600;
    margin-top: 4px;
}

/* ==================================================
   FOOTER
   ================================================== */

.footer-container {
    background-color: #1c3320;
    color: #e2e8df;
    padding: 40px 20px 25px 20px;
    margin-top: 80px;
    text-align: center;
}

.footer-brand {
    font-size: 22px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 10px;
}

.footer-text {
    font-size: 14px;
    color: #a3b59b;
    margin-bottom: 20px;
}

.footer-copy {
    font-size: 13px;
    color: #788a71;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 20px;
}

/* ==================================================
   REGRAS DE RESPONSIVIDADE (MOBILE)
   ================================================== */

@media (max-width: 768px) {
    .block-container {
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }

    .logo-text {
        font-size: 24px;
        text-align: center;
    }

    div[data-testid="stButton"] button {
        min-height: 45px !important;
    }

    div[data-testid="stButton"] button p,
    div[data-testid="stButton"] button span {
        font-size: 13px !important;
    }

    .about-card {
        padding: 24px 16px;
        margin: 30px 10px;
        border-radius: 16px;
    }

    .about-title {
        font-size: 24px;
    }

    .about-text {
        font-size: 15px;
        line-height: 1.6;
    }

    .stats-grid {
        grid-template-columns: 1fr;
        gap: 12px;
    }

    .stat-item {
        padding: 16px;
    }
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER (Navegação)
# ==================================================

col_logo, c1, c2, c3, c4, c5 = st.columns([3.5, 1, 1, 1, 1, 1])

with col_logo:
    col_img, col_txt = st.columns([0.5, 4])

    logo_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "logo.png"
    )

    with col_img:
        if os.path.exists(logo_path):
            st.image(logo_path, width=70)
        else:
            st.write("🏔️")

    with col_txt:
        st.markdown(
            """
            <div style="padding-top: 14px;">
                <div class="logo-text">Capivaras Trek</div>
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
# HELPER BASE64
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
# CARROSSEL HERO (RESPONSIVO)
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
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
          border-radius: 28px;
          overflow: hidden;
          box-shadow: 0 15px 35px rgba(0,0,0,0.18);
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

        .slide-1 {{ background-position: center 40%; }}
        .slide-2 {{ background-position: center 40%; }}
        .slide-3 {{ background-position: center 65%; }}

        .swiper-slide::before {{
          content: "";
          position: absolute;
          inset: 0;
          background: linear-gradient(
            180deg, 
            rgba(0, 0, 0, 0.25) 0%, 
            rgba(0, 0, 0, 0.45) 50%, 
            rgba(0, 0, 0, 0.6) 100%
          );
          z-index: 1;
        }}

        .hero-title-container {{
          position: relative;
          z-index: 2;
          text-align: center;
          padding: 0 20px;
        }}

        .hero-title {{
          font-size: 56px;
          font-weight: 900;
          letter-spacing: 4px;
          text-transform: uppercase;
          line-height: 1.15;
          color: #ffffff;
          text-shadow: 0 6px 20px rgba(0, 0, 0, 0.7);
        }}

        .swiper-pagination {{
          position: relative !important;
          margin-top: 18px !important;
          bottom: 0 !important;
        }}

        .swiper-pagination-bullet {{
          width: 12px;
          height: 12px;
          background: #1c3320;
          opacity: 0.35;
          transition: all 0.3s ease;
        }}

        .swiper-pagination-bullet-active {{
          background: #1c3320 !important;
          opacity: 1;
          width: 28px;
          border-radius: 6px;
        }}

        .swiper-button-next, .swiper-button-prev {{
          color: #ffffff !important;
          background: rgba(0, 0, 0, 0.25);
          width: 48px;
          height: 48px;
          border-radius: 50%;
          backdrop-filter: blur(4px);
          transition: all 0.2s ease;
        }}

        .swiper-button-next:after, .swiper-button-prev:after {{
          font-size: 20px !important;
          font-weight: bold;
        }}

        /* AJUSTES EXCLUSIVOS PARA TELAS DE CELULAR */
        @media (max-width: 768px) {{
          .swiper {{
            border-radius: 16px;
          }}

          .swiper-slide {{
            height: 420px;
          }}

          .hero-title {{
            font-size: 32px;
            letter-spacing: 2px;
          }}

          .swiper-button-next, .swiper-button-prev {{
            width: 36px;
            height: 36px;
          }}

          .swiper-button-next:after, .swiper-button-prev:after {{
            font-size: 14px !important;
          }}
        }}
      </style>
    </head>
    <body>

      <div class="swiper mySwiper">
        <div class="swiper-wrapper">

          <!-- SLIDE 1 -->
          <div class="swiper-slide slide-1" style="background-image: url('{img1}');">
            <div class="hero-title-container">
              <h1 class="hero-title">CUME<br>DO<br>TAIPABUÇU</h1>
            </div>
          </div>

          <!-- SLIDE 2 -->
          <div class="swiper-slide slide-2" style="background-image: url('{img2}');">
            <div class="hero-title-container">
              <h1 class="hero-title">CACHOEIRA<br>DA<br>LAPINHA</h1>
            </div>
          </div>

          <!-- SLIDE 3 -->
          <div class="swiper-slide slide-3" style="background-image: url('{img3}');">
            <div class="hero-title-container">
              <h1 class="hero-title">CUME<br>DO<br>ANHANGAVA</h1>
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
          speed: 800,
          autoplay: {{
            delay: 6500,
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
# SEÇÃO: QUEM SOMOS
# ==================================================

about_html = """
<div class="about-card">
<div class="about-title">Quem Somos</div>
<div class="about-subtitle-line"></div>
<p class="about-text">
O <strong>Capivaras Trek</strong> nasceu da paixão visceral pelas montanhas, pelas matas preservadas e pela liberdade incomparável que só a caminhada ao ar livre proporciona. Somos um grupo de praticantes de trekking e montanhismo dedicados a desbravar novas rotas, superar limites com segurança e promover o ecoturismo consciente.
</p>
<p class="about-text">
Acreditamos que cada trilha percorrida é uma oportunidade de reconexão, amizade e aprendizado. Seja no desafio técnico de cumes imponentes ou na contemplação silenciosa de cachoeiras, nosso compromisso é viver a montanha respeitando a fauna, a flora e as comunidades locais.
</p>
<div class="stats-grid">
<div class="stat-item">
<div class="stat-icon">🧗‍♂️</div>
<div class="stat-number">+50</div>
<div class="stat-label">Cumes Conquistados</div>
</div>
<div class="stat-item">
<div class="stat-icon">🥾</div>
<div class="stat-number">100%</div>
<div class="stat-label">Espírito de Equipe</div>
</div>
<div class="stat-item">
<div class="stat-icon">🌿</div>
<div class="stat-number">Mínimo Impacto</div>
<div class="stat-label">Turismo Consciente</div>
</div>
</div>
</div>
"""

st.markdown(about_html, unsafe_allow_html=True)

# ==================================================
# RODAPÉ (FOOTER)
# ==================================================

footer_html = """
<div class="footer-container">
<div class="footer-brand">CAPIVARAS TREK</div>
<div class="footer-text">Explorando a montanha com respeito, consciência e paixão.</div>
<div class="footer-copy">
© 2026 Capivaras Trek — Todos os direitos reservados.
</div>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)

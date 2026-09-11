import streamlit as st
import streamlit.components.v1 as components

# ==================================================
# COMPONENTE DE CARROSSEL MODERNO (SWIPER.JS)
# ==================================================

def render_hero_carousel():
    # Código HTML/CSS/JS do carrossel
    carousel_html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
      <meta charset="UTF-8">
      <!-- Swiper CSS -->
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
      <style>
        * {
          box-sizing: border-box;
          margin: 0;
          padding: 0;
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        body {
          background: transparent;
          padding: 10px 0;
        }

        .swiper {
          width: 100%;
          border-radius: 24px; /* Bordas arredondadas como na imagem */
          overflow: hidden;
          box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }

        .swiper-slide {
          position: relative;
          height: 520px;
          background-size: cover;
          background-position: center;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          padding: 40px 50px;
          color: #ffffff;
        }

        /* Overlay escuro para melhorar leitura do texto */
        .swiper-slide::before {
          content: "";
          position: absolute;
          inset: 0;
          background: linear-gradient(180deg, rgba(0, 0, 0, 0.4) 0%, rgba(0, 0, 0, 0.6) 100%);
          z-index: 1;
        }

        .slide-content {
          position: relative;
          z-index: 2;
          height: 100%;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
        }

        /* Título Principal Centralizado */
        .hero-title-container {
          text-align: center;
          margin-top: 20px;
        }

        .hero-title {
          font-size: 56px;
          font-weight: 900;
          letter-spacing: 2px;
          text-transform: uppercase;
          line-height: 1.1;
          text-shadow: 0 4px 10px rgba(0,0,0,0.5);
        }

        .hero-subtitle-tag {
          display: inline-block;
          background-color: #ff5e00; /* Laranja em destaque */
          color: white;
          font-size: 22px;
          font-weight: 800;
          padding: 8px 24px;
          border-radius: 8px;
          margin-top: 15px;
          box-shadow: 0 4px 12px rgba(255, 94, 0, 0.4);
        }

        /* Footer do Card com Informações */
        .card-footer {
          display: flex;
          flex-direction: column;
          gap: 15px;
          align-items: flex-start;
        }

        .btn-explorar {
          background-color: #ff5e00;
          color: #fff;
          border: none;
          padding: 12px 28px;
          font-size: 16px;
          font-weight: 700;
          border-radius: 12px;
          cursor: pointer;
          transition: transform 0.2s, background-color 0.2s;
          text-decoration: none;
        }

        .btn-explorar:hover {
          background-color: #e05300;
          transform: translateY(-2px);
        }

        .info-badges {
          display: flex;
          gap: 20px;
          align-items: center;
          flex-wrap: wrap;
        }

        .badge-group {
          display: flex;
          align-items: center;
          gap: 8px;
          font-size: 14px;
          font-weight: 700;
        }

        .badge-pill {
          background: rgba(255, 255, 255, 0.25);
          backdrop-filter: blur(8px);
          padding: 6px 14px;
          border-radius: 20px;
          font-size: 13px;
          font-weight: 600;
          border: 1px solid rgba(255, 255, 255, 0.3);
        }

        /* Estilização da Paginação (Bolinhas) fora/dentro */
        .swiper-pagination {
          position: relative !important;
          margin-top: 15px !important;
          bottom: 0 !important;
        }

        .swiper-pagination-bullet {
          width: 12px;
          height: 12px;
          background: #ccc;
          opacity: 0.6;
        }

        .swiper-pagination-bullet-active {
          background: #ff5e00 !important;
          opacity: 1;
          width: 14px;
          height: 14px;
        }

        /* Setas de Navegação */
        .swiper-button-next, .swiper-button-prev {
          color: #ffffff !important;
          transform: scale(0.6);
          z-index: 10;
        }
      </style>
    </head>
    <body>

      <!-- Slider container -->
      <div class="swiper mySwiper">
        <div class="swiper-wrapper">

          <!-- SLIDE 1 -->
          <div class="swiper-slide" style="background-image: url('https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?q=80&w=1600');">
            <div class="slide-content">
              
              <div class="hero-title-container">
                <h1 class="hero-title">ACAMPAMENTO<br>DE ANO NOVO</h1>
                <div class="hero-subtitle-tag">Chácara Araçá</div>
              </div>

              <div class="card-footer">
                <button class="btn-explorar">Explorar</button>
                <div class="info-badges">
                  <div class="badge-group">
                    📅 Próximas saídas:
                    <span class="badge-pill">Dezembro 2026</span>
                  </div>
                  <div class="badge-group">
                    📍 Locais:
                    <span class="badge-pill">Brasil</span>
                    <span class="badge-pill">Tijucas Do Sul</span>
                  </div>
                </div>
              </div>

            </div>
          </div>

          <!-- SLIDE 2 -->
          <div class="swiper-slide" style="background-image: url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1600');">
            <div class="slide-content">
              
              <div class="hero-title-container">
                <h1 class="hero-title">TRAVESSIA DA<br>SERRA DO MAR</h1>
                <div class="hero-subtitle-tag">Pico Paraná</div>
              </div>

              <div class="card-footer">
                <button class="btn-explorar">Explorar</button>
                <div class="info-badges">
                  <div class="badge-group">
                    📅 Próximas saídas:
                    <span class="badge-pill">Janeiro 2027</span>
                  </div>
                  <div class="badge-group">
                    📍 Locais:
                    <span class="badge-pill">Brasil</span>
                    <span class="badge-pill">Antonina</span>
                  </div>
                </div>
              </div>

            </div>
          </div>

        </div>

        <!-- Setas de Navegação -->
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
      </div>

      <!-- Bolinhas de Paginação (no rodapé inferior externamente) -->
      <div class="swiper-pagination"></div>

      <!-- Swiper JS -->
      <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
      <script>
        var swiper = new Swiper(".mySwiper", {
          loop: true,
          autoplay: {
            delay: 4000,
            disableOnInteraction: false,
          },
          pagination: {
            el: ".swiper-pagination",
            clickable: true,
          },
          navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
          },
        });
      </script>
    </body>
    </html>
    """
    
    # Renderiza o HTML no Streamlit com altura adequada
    components.html(carousel_html, height=600)

# Chame a função onde deseja exibir o carrossel no seu app
render_hero_carousel()

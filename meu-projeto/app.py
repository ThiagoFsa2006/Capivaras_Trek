import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Capivaras Trek",
    page_icon="🐾",
    layout="wide"
)

# 1. Header / Barra de Navegação
st.title("Capivaras Trek 🐾")
st.caption("Explore a Natureza, Siga as Capivaras")

# Menu de navegação superior usando colunas
col_nav1, col_nav2, col_nav3, col_nav4, col_nav5, col_nav6 = st.columns(6)
with col_nav1:
    st.button("Home", use_container_width=True)
with col_nav2:
    st.button("Trilhas", use_container_width=True)
with col_nav3:
    st.button("Acervo", use_container_width=True)
with col_nav4:
    st.button("Calendário", use_container_width=True)
with col_nav5:
    st.button("Blog", use_container_width=True)
with col_nav6:
    st.button("Contato", use_container_width=True)

st.divider()

# 2. Carrossel / Banner de Imagens
with st.container(border=True):
    st.markdown("<h2 style='text-align: center; color: gray;'>IMG IMG</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center;'>(Slider de Imagens: Trilhas em Destaque | Aventuras | Natureza)</p>", unsafe_allow_html=True)

st.divider()

# 3. Grid de Conteúdo Principal (2 Colunas x 2 Linhas)
col_left, col_right = st.columns(2)

# --- Linha 1: Trilhas em Destaque & Acervo ---
with col_left:
    with st.container(border=True):
        st.subheader("⛰️ Trilhas em Destaque")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.button("Pedra da Gávea", use_container_width=True)
        with c2:
            st.button("Serra dos Órgãos", use_container_width=True)
        with c3:
            st.button("Pico da Bandeira", use_container_width=True)
        st.button("Ver Todas as Trilhas", type="primary", use_container_width=True)

with col_right:
    with st.container(border=True):
        st.subheader("📖 Artigos & Dicas")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.button("Equipamentos", use_container_width=True)
        with c2:
            st.button("Dicas de Camp", use_container_width=True)
        with c3:
            st.button("Flora & Fauna", use_container_width=True)
        st.button("Acessar Acervo", type="primary", use_container_width=True)

# --- Linha 2: Calendário & Wikiloc ---
with col_left:
    with st.container(border=True):
        st.subheader("📅 Próximas Aventuras")
        st.write("• **15 Out** - Trilha Ilha Grande")
        st.write("• **22 Out** - Pico das Agulhas Negras")
        st.write("• **05 Nov** - Circuito das Cachoeiras")
        st.button("Ver Agenda Completa", use_container_width=True)

with col_right:
    with st.container(border=True):
        st.subheader("🗺️ Mapas & Rotas (Wikiloc)")
        st.info("Mapa Trilha X\n\n(Ícone Wikiloc, Dificuldade, Duração, Mapa simplificado)")
        st.button("Ver no Wikiloc", use_container_width=True)

st.divider()

# 4. Seção Inferior: Blog Recente & Rodapé
col_blog, col_footer = st.columns(2)

with col_blog:
    with st.container(border=True):
        st.subheader("📝 Blog Recente")
        b1, b2 = st.columns(2)
        with b1:
            st.button("📝 Post 1", use_container_width=True)
        with b2:
            st.button("📝 Post 2", use_container_width=True)

with col_footer:
    with st.container(border=True):
        st.write("**Navegação Rápida:** Home | Trilhas | Acervo | Blog | Contato")
        st.caption("© 2026 Capivaras Trek. Todos os direitos reservados.")

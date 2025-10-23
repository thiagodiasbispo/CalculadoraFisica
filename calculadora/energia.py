import streamlit as st

def render_energia_trabalho():
    st.title("Calculadora de Energia / Trabalho (exemplo)")
    left, right = st.columns([1,1])
    with left:
        st.header("Energia e Trabalho")
        st.write("Conteúdo didático em desenvolvimento.")
    with right:
        st.header("Entrada (exemplo)")
        st.info("Placeholder - cálculo será implementado conforme necessidade.")
    if st.button("Voltar à página principal"):
        st.query_params["page"] = "home"
        st.rerun()

def render_subarea(slug: str):
    if slug == "energia_trabalho":
        render_energia_trabalho()
    else:
        st.error(f"Sub-área '{slug}' não encontrada em energia.")
        if st.button("Voltar à página principal"):
            st.query_params["page"] = "home"
            st.rerun()
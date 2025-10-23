import streamlit as st

def render_ohm():
    st.title("Calculadora de Lei de Ohm (exemplo)")
    left, right = st.columns([1,1])
    with left:
        st.header("Sobre a Lei de Ohm")
        st.write("Em desenvolvimento - exemplo de conteúdo didático.")
    with right:
        st.header("Entrada (exemplo)")
        st.info("Esta página é um placeholder para mostrar estrutura modular. Em futuras versões implementaremos as funções de cálculo.")
    if st.button("Voltar à página principal"):
        st.query_params["page"] = "home"
        st.rerun()

def render_subarea(slug: str):
    if slug == "ohm":
        render_ohm()
    else:
        st.error(f"Sub-área '{slug}' não encontrada em eletrônica.")
        if st.button("Voltar à página principal"):
            st.query_params["page"] = "home"
            st.rerun()
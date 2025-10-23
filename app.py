import streamlit as st
from importlib import import_module

st.set_page_config(page_title="Calculadora Física", layout="wide")

# Mapeamento de ramos -> lista de (slug, nome_exibicao)
RAMOS = {
    "eletromagnetismo": {
        "title": "Calculadoras de eletromagnetismo 🧲",
        "subareas": [
            ("watts", "Calculadora de Watts")
        ],
    },
    "eletronica": {
        "title": "Calculadoras de eletrônica e circuitos 💡",
        "subareas": [
            ("ohm", "Calculadora de Lei de Ohm (exemplo)"),
        ],
    },
    "energia": {
        "title": "Calculadoras de energia, trabalho e potência ⚡",
        "subareas": [
            ("energia_trabalho", "Calculadora de Energia / Trabalho (exemplo)")
        ],
    },
}

def render_home():
    st.title("Calculadora Física")
    st.write("Escolha um ramo e uma sub-área para abrir a calculadora correspondente.")
    for ramo_slug, ramo_data in RAMOS.items():
        st.subheader(ramo_data["title"])
        # Apresenta sub-areas como lista não ordenada com links
        for slug, nome in ramo_data["subareas"]:
            link = f"?page={ramo_slug}/{slug}"
            st.markdown(f"- [{nome}]({link})")

def route_page(page_param: str):
    # page_param expected like "eletromagnetismo/watts"
    parts = page_param.split("/")
    if len(parts) != 2:
        st.error("Página inválida. Voltando para a página principal.")
        render_home()
        return

    ramo, subarea = parts
    try:
        module = import_module(f"calculadora.{ramo}")
    except Exception as e:
        st.error(f"Erro ao carregar módulo para o ramo '{ramo}': {e}")
        return

    # Cada módulo implementa função render_subarea(slug)
    if hasattr(module, "render_subarea"):
        module.render_subarea(subarea)
    else:
        st.error(f"O módulo do ramo '{ramo}' não implementa 'render_subarea'.")

def main():
    params = st.query_params
    page = params.get("page", "home")
    if page == "home" or page.strip() == "":
        render_home()
    else:
        route_page(page)

if __name__ == "__main__":
    main()
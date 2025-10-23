import streamlit as st

# Permitir entradas vazias para que o cálculo só ocorra quando variáveis necessárias estiverem preenchidas
def parse_optional_float(label, key, help_text=""):
    txt = st.text_input(label=label, key=key, help=help_text)
    txt = txt.strip()
    if txt == "":
        return None
    try:
        val = float(txt.replace(",", "."))
        return val
    except Exception:
        st.error(f"Entrada inválida em '{label}': insira um número (use '.' ou ',' como separador decimal).")
        return None
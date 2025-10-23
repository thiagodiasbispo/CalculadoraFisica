import streamlit as st
from .comum import parse_optional_float

# --- Funções de cálculo (regras da física) ---
def calc_power_from_v_i(v: float, i: float) -> float:
    """Potência P = v * i"""
    return v * i


def calc_power_from_i_r(i: float, r: float) -> float:
    """Potência P = i^2 * r"""
    return (i ** 2) * r


def calc_power_from_v_r(v: float, r: float) -> float:
    """Potência P = v^2 / r"""
    return (v ** 2) / r


def compute_power(V, I, R):
    """
    Determina a potência com base nas variáveis disponíveis.
    Retorna (P_value, method) onde method descreve a fórmula usada.
    Se não for possível calcular, retorna (None, None).
    """
    # V, I, R podem ser None ou float
    if V is not None and I is not None:
        return calc_power_from_v_i(V, I), "P = V × I"
    if I is not None and R is not None:
        return calc_power_from_i_r(I, R), "P = I² × R"
    if V is not None and R is not None:
        # evitar divisão por zero
        if R == 0:
            return None, "R não pode ser zero na fórmula P = V² / R"
        return calc_power_from_v_r(V, R), "P = V² / R"
    return None, None


# --- Interface da sub-área "watts" ---
def render_watts():
    st.title("Calculadora de Watts (Potência elétrica)")

    # Layout em duas colunas
    left, right = st.columns([1, 1])

    with left:
        st.header("Informações didáticas")
        st.markdown(
            """
            A potência elétrica (P), medida em Watts (W), descreve a taxa de energia elétrica transferida ou consumida.

            Fórmulas comuns:
            - P = V × I  (voltagem vezes corrente)
            - P = I² × R (corrente ao quadrado vezes resistência)
            - P = V² / R (voltagem ao quadrado dividida pela resistência)

            Use quaisquer duas grandezas conhecidas para calcular a potência. Se todos os campos forem deixados em branco ou insuficientes, a potência não poderá ser determinada.
            """
        )
        st.markdown("Unidades:")
        st.write("- V: Volts (V)")
        st.write("- I: Corrente (A)")
        st.write("- R: Resistência (Ω)")
        st.info(
            "A calculadora irá atualizar automaticamente o valor de P assim que entradas suficientes forem fornecidas.")

    with right:
        st.header("Entradas (deixe em branco se desconhecido)")

        v = parse_optional_float("Voltagem V (V)", key="v_voltage", help_text="Ex: 12, 230")
        i = parse_optional_float("Corrente I (A)", key="i_current", help_text="Ex: 1.5")
        r = parse_optional_float("Resistência R (Ω)", key="r_resistance", help_text="Ex: 100")

        p_value, method = compute_power(v, i, r)

        st.markdown("---")
        if p_value is None and method is None:
            st.warning("Insira pelo menos duas das variáveis (V, I, R) para calcular a potência automaticamente.")
        elif p_value is None and method is not None:
            st.error(f"Não foi possível calcular: {method}")
        else:
            st.success(f"Potência calculada: {p_value:.6g} W")
            st.caption(f"Usando a fórmula: {method}")

    # Botão para voltar à página principal
    if st.button("Voltar à página principal"):
        st.query_params["page"] = "home"
        st.rerun()


# --- Função de roteamento do módulo ---
def render_subarea(slug: str):
    if slug == "watts":
        render_watts()
    else:
        st.error(f"Sub-área '{slug}' não encontrada em eletromagnetismo.")
        if st.button("Voltar à página principal"):
            st.query_params["page"] = "home"
            st.rerun()
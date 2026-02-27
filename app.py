import streamlit as st

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="RAIO X FINANCEIRO",
    page_icon="📊",
    layout="wide"
)

st.title("📊 RAIO X FINANCEIRO")
st.markdown("### Análise Simplificada da empresa")

st.divider()

# =========================
# ENTRADA DE DADOS
# =========================

col1, col2 = st.columns(2)

with col1:
    empresa = st.text_input("Empresa")
    setor = st.text_input("Setor")
    preco = st.number_input("Preço Atual", min_value=0.0)
    market_cap = st.number_input("Market Cap", min_value=0.0)
    pl = st.number_input("P/L", min_value=0.0)
    pvp = st.number_input("P/VP", min_value=0.0)

with col2:
    roe = st.number_input("ROE (%)", min_value=0.0) / 100
    margem = st.number_input("Margem Líquida (%)", min_value=0.0) / 100
    divida = st.number_input("Dívida Total", min_value=0.0)
    caixa = st.number_input("Caixa", min_value=0.0)
    receita = st.number_input("Receita", min_value=0.0)
    lucro = st.number_input("Lucro Líquido", min_value=0.0)

st.divider()

# =========================
# FUNÇÃO DE SCORE
# =========================

def calcular_score():
    score = 0

    # ROE
    if roe >= 0.20:
        score += 30
    elif roe >= 0.10:
        score += 20
    elif roe > 0:
        score += 10

    # Margem
    if margem >= 0.20:
        score += 25
    elif margem >= 0.10:
        score += 15
    elif margem > 0:
        score += 5

    # Dívida líquida
    divida_liquida = divida - caixa

    if divida_liquida <= 0:
        score += 20
    elif receita > 0 and divida_liquida < receita:
        score += 10

    # Valuation
    if pl > 0:
        if pl <= 15:
            score += 15
        elif pl <= 25:
            score += 8

    # P/VP
    if pvp > 0:
        if pvp <= 1.5:
            score += 10
        elif pvp <= 3:
            score += 5

    return score

def diagnostico(score):
    if score >= 75:
        return "🟢 EXCELENTE", "Empresa sólida e bem estruturada."
    elif score >= 50:
        return "🟡 BOA", "Empresa razoável, mas exige atenção."
    else:
        return "🔴 RISCO", "Empresa com fundamentos frágeis."

# =========================
# BOTÃO DE ANÁLISE
# =========================

if st.button("🔎 Analisar Empresa"):

    score = calcular_score()
    status, mensagem = diagnostico(score)

    st.divider()

    st.subheader("Resultado da Análise")

    colA, colB, colC = st.columns(3)

    with colA:
        st.metric("Score Financeiro", score)

    with colB:
        st.metric("Classificação", status)

    with colC:
        if receita > 0:
            margem_calculada = lucro / receita
            st.metric("Margem Real", f"{margem_calculada:.2%}")
            

    st.success(mensagem)



import streamlit as st


    
from modelos import Empresa
from calculos import calcular_score, diagnostico

st.title("RAIO X FINANCEIRO")

nome = st.text_input("Empresa")
setor = st.text_input("Setor")

preco = st.number_input("Preço Atual")
market_cap = st.number_input("Market Cap")

pl = st.number_input("P/L")
pvp = st.number_input("P/VP")
roe = st.number_input("ROE (%)") / 100
margem = st.number_input("Margem Líquida (%)") / 100

divida = st.number_input("Dívida Total")
caixa = st.number_input("Caixa")

receita = st.number_input("Receita")
lucro = st.number_input("Lucro Líquido")


if st.button("Analisar"):

    empresa = Empresa(
        nome,
        setor,
        preco,
        market_cap,
         pl,
        pvp,
        roe,
        margem,
        divida,
        caixa,
        receita,
        lucro
    )

    score = calcular_score(empresa)

    status, texto = diagnostico(score)

    st.metric("Score Financeiro", score)

    st.write("Classificação:", status)
    st.write("Diagnóstico:", texto)
    




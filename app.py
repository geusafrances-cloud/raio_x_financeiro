import streamlit as st

st.title("RAIO X FINANCEIRa")

empresa = st.text_input("Empresa")

if st.button("Testar"):

    st.write("Empresa:", empresa)

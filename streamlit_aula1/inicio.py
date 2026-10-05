import streamlit as st
import pandas as pd

st.title("Meu primeiro dash")
st.subheader("Matheus")

st.write("Olá, mundo")

nome ="Matheus"
idade ="17"

st.write("Olá",nome ,"a minha idade e", idade,"anos")


df = pd.DataFrame({
   'Materias': ["Português", "Matemática", "Python ", "Frame"],
   'notas': [ 5, 9, 7, 10]
 })
df

produtos =  {
  "Arroz (1kg)": 4.50,
    "Feijão (1kg)": 7.20,
    "Óleo de Soja": 5.80,
    "Açúcar (1kg)": 3.10,
    "Café (500g)": 10.50
}

item_selecionado = st.multiselect(
    "Selecione os itens:",
    options=list(produtos.keys())
    
)

if item_selecionado:
    precos = [produtos[item] for item in item_selecionado]
    total = sum(precos)
    st.write(f"Valor total: R$", total)
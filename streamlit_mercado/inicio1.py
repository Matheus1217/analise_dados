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

st.title("Calculo da compra")


itens_escolhidos = st.multiselect(
    "Selecione os itens:",
    options=list(produtos.keys())
)

col1, col2 = st.columns(2)


with col1:
 dinheiroC = st.number_input("Quanto você tem?", value=0.0, step=1.0)

with col2:
 Ctroco = st.number_input("Quanto vai gastar?", value=0.0, step=1.0)
 
 
operacao = st.selectbox(
    "Escolha como quer calcular a compra",
    options=["Adição (+)", "Subtração (-)", "Multiplicação (x)", "Divisão (/)"]
)

if st.button("Calcular", type="primary"):
    resultado = None
    
    if operacao == "Adição (+)":
        resultado = dinheiroC + Ctroco
        st.write("O Resultado é: ", resultado)  
        
    elif operacao == "Subtração (-)":
        resultado = dinheiroC - Ctroco
        st.write("O troco é: ", resultado)
        
    elif operacao == "Multiplicação (x)":
        resultado = dinheiroC * Ctroco
        st.write("O Resultado é: ", resultado)
        
    elif operacao == "Divisão (/)":
        if Ctroco != 0:
            resultado = dinheiroC / Ctroco
            st.write("O Resultado é: ", resultado)
            
        else:
            st.error("Erro: Não é possível dividir por zero")
            erro = True



if itens_escolhidos:
    precos = [produtos[item] for item in itens_escolhidos]
    total = sum(precos)
    st.write(f"Valor Total: R$", total)
    
    
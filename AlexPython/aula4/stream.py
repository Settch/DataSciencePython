# Biblioteca para criação de Dashboards
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv("vendas_loja.csv")
df["Receita"] = df["Quantidade"] * df["Preco_Unitario"]
df["Data"] = pd.to_datetime(df["Data"])
df["Mês"] = df["Data"].dt.to_period("M")

st.title("Dashboard de Vendas")

# Infos principais
st.metric("Total de Vendas", f"R$ {df['Receita'].sum():,.2f}")
st.metric("Média por Venda", f"R$ {df['Receita'].mean():,.2f}")

#filtro por categoria
categorias = df["Categoria"].unique() #Categoria é unicas
categoria_selecionada = st.selectbox("Selecione a categoria:", categorias)

df_filtrado = df[df['Categoria'] == categoria_selecionada]

#Gráfico por produto
st.subheader("Receita por Produto")
# criar uma figura, que vai o gráfico
fig1, ax1 = plt.subplots()
df_filtrado.groupby("Produto")["Receita"].sum().plot(kind="bar", ax=ax1)
st.pyplot(fig1)

#Gráfico por mês
st.subheader("Receita Mensal")
fig2, ax2 = plt.subplots()
df.groupby("Mês")['Receita'].sum().plot(ax=ax2)
st.pyplot(fig2)


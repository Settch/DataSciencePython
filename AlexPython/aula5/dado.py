import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('vendas_lojinha.csv')

df['Receita'] = df['Quantidade'] * df['Preço']

df['Ticket'] = df['Receita'] / df['Quantidade']


total_receita = df['Receita'].sum()


df['Data'] = pd.to_datetime(df['Data'])
df['Mes'] = df['Data'].dt.to_period("M")
df['Ano'] = df['Data'].dt.to_period("Y")


receita_mensal = df.groupby("Mes")["Receita"].sum()

produto_mais_vendido = df.groupby("Produto")["Receita"].sum().idxmax()

quantidade_produtos = df.groupby("Produto")["Quantidade"].sum()

receita_categoria = df.groupby("Categoria")["Receita"].sum()

ticket_mensal = df.groupby("Mes")["Ticket"].mean()


df.groupby("Categoria")["Receita"].sum().plot(kind="bar", title="Receita por categoria")
plt.ylabel("Receita (R$)")
plt.tight_layout()
plt.show()


df.groupby("Mes")["Receita"].sum().plot(kind="line", title="Receita Mensal")
plt.ylabel("Receita (R$)")
plt.tight_layout()
plt.show()

df.groupby("Categoria")["Receita"].sum().plot(kind="pie", autopct='%1.1f%%', title="Participação de cada categoria na Receita total")
plt.tight_layout()
plt.show() 
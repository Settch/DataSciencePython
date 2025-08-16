import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('dados_aula_escola.csv')

print("5 primeiras linhas do Dados do DataFrame:")
print(df.head())
print(df.info())
print(df.describe())

print("Alunos com nota maior que 7:")
print(df[df['Nota'] > 7])

print("Alunos do 9º ano:")
print(df[df['Ano_Serie'] == '9º'])

print("Alunos com idade maior ou igual a 14:")
print(df[df['Idade'] >= 14])

print("Alunos com idade menor que 10 e nota menor que 5:")
print(df[(df['Idade'] < 10) & (df['Nota'] < 5)])

media_notas_series = df.groupby('Ano_Serie')['Nota'].mean()

series_maior_media = media_notas_series.idxmax()

media_alunos_idade_nota8 = df[df['Nota'] >= 8].groupby('Idade')['Nota'].mean()
print("Idade media dos alunos com nota maior ou igual a 8:")
print(media_alunos_idade_nota8)

print("Alunos em ordem descrescente de nota:")
print(df.sort_values(by='Nota', ascending=False))
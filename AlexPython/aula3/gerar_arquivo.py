import csv
import matplotlib.pyplot as plt
import os

# nome do arquivo
ARQUIVO_CSV = 'dados_senai.csv'

# salvar arquivo
def salvar_em_csv(nome, idade, email):
    # Verificar se o arquivo existe
    arquivo_existe = os.path.exists(ARQUIVO_CSV)

    # a -> acrescimo
    # newline -> evitar linhas brancas
    # encoding -> codificação caracteres BR ç, ~, ´, `
    with open(ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)

        # Se o arquivo não existir, escreve o cabeçalho
        if not arquivo_existe:
            escritor.writerow(['nome', 'idade', 'email'])

        # Escreve os dados do usuário
        escritor.writerow([nome, idade, email])

# queremos identificar a faixa etária dos usuários do sistema

def mostra_grafico():
    # Le idades
    faixas = {
        '0-17': 0,
        '18-30': 0,
        '31-45': 0,
        '46-60': 0,
        '60+': 0,
    }

    # mode r -> Read -> Leitura
    with open(ARQUIVO_CSV, mode='r', encoding='utf-8') as arquivo:
        # ler o doc
        leitor = csv.DictReader(arquivo)

        # enquanto tiver linhas, ele percorre
        for linha in leitor:
            try:
                idade = int(linha['idade'])  # capturar a idade da coluna
                if idade <= 17:             # verifico a etapa
                    faixas['0-17'] += 1     # caso ela esteja, soma mais uma
                elif idade <= 30:
                    faixas['18-30'] += 1
                elif idade <= 45:
                    faixas['31-45'] += 1    
                elif idade <= 60:
                    faixas['46-60'] += 1
                else:
                    faixas['60+'] += 1
            except ValueError:
                continue

        plt.bar(faixas.keys(), faixas.values(), color='skyblue')
        plt.title('Distribuição por Faixa Etária')
        plt.xlabel('Faixa Etária')
        plt.ylabel('Quantidade de Pessoas')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

# funcao principal
def main():
    # repetir infinitamente
    while True:
        print("\nDigite os dados do usuário:")
        nome = input("Nome: ")
        idade = input("Idade: ")
        email = input("Email: ")

        # chamando a função para salvar no arquivo csv
        salvar_em_csv(nome, idade, email)
        print("Dados salvos com sucesso!")

        continuar = input("Deseja adicionar outro? s/n")
        if continuar != 's':
            break

    mostra_grafico()

if __name__ == '__main__':
    main()

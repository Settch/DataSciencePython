# ID_Aluno, Nome, Idade, Ano_Serie, Nota
import csv
# Path lib para salvar o CSV em uma pasta/caminho
from pathlib import Path

# Arquivo do CSV
ARQUIVO = Path("dados_escola.csv")
# Campos dos nossos arquivos 
CAMPOS = ["ID_Aluno", "Nome", "Idade", "Ano_Serie", "Nota"]

# Sistema vai executar ao iniciar
def carregar_arquivo():
    """Carregar o arquivo existente"""  
    if not ARQUIVO.exists(): # Verifica se o arquivo existe
        return [], 1 # Lista vazia
    # significa que o arquivo existe
    with ARQUIVO.open(newline="", encoding="utf-8") as arquivo:
        #leitor, ler o arquivo csv existente
        leitor = csv.DictReader(arquivo)
        # capturar os dados, transformar em lista
        dados = list(leitor)
    # ListaDados, ID
    return dados, len(dados) + 1

def salvar(dados):
    """ Salvar os dados no CSV """
    with ARQUIVO.open("w", newline="", encoding="utf-8") as arquivo:
        # com o arquivo aberto
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        # escrever os dados
        escritor.writerows(dados)

def main():
    dados, proximo_id = carregar_arquivo()
    print("Arquivo: ", ARQUIVO.resolve())
    print("Campos: ", CAMPOS)

    print("Para parar o sistema, deixe o campo vazio e pressione Enter.")

    # repetir infinito
    while True:
        # Capturar os dados do usuário
        id_aluno = input(f"ID Aluno [{proximo_id}]: ") or proximo_id
        nome = input("Nome: ")
        idade = input("Idade: ")
        ano_serie = input("Ano/Série: ")
        nota = input("Nota: ")

        # Verifica se o usuário deixou algum campo vazio
        if not nome or not idade or not ano_serie or not nota:
            print("Sistema encerrado.")
            break

        # Adiciona os dados na lista
        dados.append({
            "ID_Aluno": id_aluno,
            "Nome": nome,
            "Idade": idade,
            "Ano_Serie": ano_serie,
            "Nota": nota
        })

        # Salva os dados no CSV
        salvar(dados)
        print("Dados salvos com sucesso!")
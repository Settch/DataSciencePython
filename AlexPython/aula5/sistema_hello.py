#desenha tela GUI ( Graphical User Interface)
import tkinter as tk
from tkinter import messagebox

# exibir o nome da pessoa
def mostrar_mensagem():
    nome = entrada_nome.get()
    messagebox.showinfo("Saudação", f"Ola, {nome} bem vindo!")

janela = tk.Tk()
# criar uma janela
janela.title("Olá tkinter")
janela.geometry("300x150") # 300 pixels por 150 pixels

#criar o label do input
rotulo_nome = tk.Label(janela, text="Digite o seu nome:")
rotulo_nome.pack(pady=5) #configurando estilo do texto

#criando campo de texto
entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

botao = tk.Button(janela, text="Clique aqui", command=mostrar_mensagem)
botao.pack(pady=20)

#inicia o tk
janela.mainloop()
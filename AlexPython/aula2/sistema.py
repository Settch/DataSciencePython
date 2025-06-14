
def menu():
    print("====================================")
    print("Sistema do Café, Chá e Lasanha SENAI")
    print("====================================")
    print("1 - Criar um Café")
    print("2 - Listar os Cafés")
    print("3 - Qual o maior preço do Café?")
    print("0 - Sair do sistema")

class Cafe:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def __str__(self):
        #:.2-> deixar somente dois números após o ponto
        return f"{self.nome} - R$ {self.preco:.2f}"
    
class Cha:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
        
    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"
    
cafes = []

while True:
    menu()
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        nome = input("Digite o nome do café: ")
        preco = float(input("Digite o preço do café: "))
        
        novo_cafe = Cafe(nome, preco)
        cafes.append(novo_cafe)
    elif opcao == 2:
        #Listar os cafés
        
        # len -> Length -> Tamanho
        if len(cafes) == 0:
            print("Nenhum café cadastrado")
        else:
            # \n -> Quebrar linha
            print("\n--- Lista de Cafés---")
            for cafe in cafes:
                print(cafe)
    elif opcao == 3:
        #cafes[0] => primeiro objeto
        mais_caro = cafes[0]
        for cafe in cafes:
            if cafe.preco > mais_caro.preco:
                mais_caro = cafe
                
        print(f"\nCafé mais caro: {mais_caro.nome}")
        print(f"\nPreço do café: {mais_caro.preco}")
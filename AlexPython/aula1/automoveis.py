print("Qual o nome do veículo?")
str(input(""))

print("Qual o preço do veículo?")
valor = float(input(""))

""" desconto1 = (valor * 60) / 100
desconto2 = (valor * 30) / 100

valorDescontado1 = valor - desconto1
valorDescontado2 = valor - desconto2 """

desc1 = valor * 0.40
desc2 = valor * 0.70

print(f'3 opções de desconto \n-{desc1} com 60% de desconto \n-{desc2} com 30% de desconto \n-{valor} sem nenhum desconto')
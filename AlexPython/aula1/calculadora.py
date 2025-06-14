print("###########")
print("Calculadora do SENAI")
print("Digite a operação a realizar")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("###########")


opcao = int(input(""))

if opcao <= 4: 
    print("Digite o primeiro número:")
    num1 = float(input(""))
    print("Digite o segundo número:")
    num2 = float(input(""))
else:
    print("deu erro mofi")

if opcao == 1:
    
    resultado = num1 + num2
    print(f'Resultado: {resultado}')
    
elif opcao == 2:
    
    resultado = num1 - num2
    print(f'Resultado: {resultado}')

elif opcao == 3:
    resultado = num1 * num2
    print(f'Resultado: {resultado}')

elif opcao == 4:
    resultado = num1 / num2
    print(f'Resultado: {resultado}')


""" 
Cálculos em Python:
+ -> Soma
- -> Subtração
* -> Multiplicação
/ -> Divisão
** -> Potenciação
// -> Arredonda a divisão
% ->

Estrutura de Decisão
== Igualdade
=> >= > < Menor Igual, Maior Igual, Maior, Menor
"""
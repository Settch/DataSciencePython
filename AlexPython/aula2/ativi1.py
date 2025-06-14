""" 
O sistema deve pedir um número 
E deve dizer se ele é par ou impar

* Multiplicação
/ Divisão
!= diferente
=> maior igual
<= menor igual
< menor
> maior
"""

print("Type a number")
n1 = int(input())

if (((n1 % 2) == 0) == True):
    print("Número é par")
else:
    print("É impar")
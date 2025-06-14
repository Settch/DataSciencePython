import math

print("Digite o valor de A:")
A = float(input())

print("Digite o valor de B:")
B = float(input())

print("Digite o valor de C:")
C = float(input())

delta = (B ** 2) - 4 * A * C

raizDelta = math.sqrt(delta)

x1 = (-B + raizDelta) / (2 * A)

x2 = (-B - raizDelta) / (2 * A)

print(f'O valor de delta é: {delta}\nO valor de x1: {x1:.2f}\nO valor de x2: {x2:.2f}')
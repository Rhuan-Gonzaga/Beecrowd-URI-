"""
1036  - formula de bhaskara

Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

"""
import math

A,B,C = map(float,input().split())

delta = math.pow(B,2) - (4.0 * A * C)

if delta < 0 or A ==0:
    print("Impossivel calcular")
else:
    r1 = (-B + delta ** (1 / 2)) / (2 * A)
    r2 = (-B - delta ** (1 / 2)) / (2 * A)
    print("R1 = %.5f" % (r1))
    print("R2 = %.5f" % (r2))
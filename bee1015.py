"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

formula = raiz (x2-x1)** + (y2-y1)**

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

Exemplo de Entrada	
1.0 7.0
5.0 9.0

Exemplo de Saída
4.4721
"""
from math import sqrt

linha1, linha2 = input().split(), input().split()

x1 = float(linha1[0])
y1 = float(linha1[1])

x2 = float(linha2[0])
y2 = float(linha2[1])

distancia = sqrt(pow(x2-x1,2) + pow(y2-y1,2)) 
print("{:.4f}".format(distancia))
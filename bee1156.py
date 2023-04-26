""" 
1156 - Sequência S II
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8+… + 39/?

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.
"""

s = 0
j = 1
for i in range(1,40,2):
    s = float(s + i / j)
    j = j * 2


print("{:.2f}".format(s))
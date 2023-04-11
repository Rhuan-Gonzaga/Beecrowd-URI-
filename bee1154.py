"""
1154 - Idades
Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

A média deve ser impressa com dois dígitos após o ponto decimal.
"""

lista = []
n = 0

while n >= 0:
    n = int(input())
    if n >=0:
        lista.append(n)

calculo = sum(lista) / len(lista)
print('{:.2f}'.format(calculo))   







    
    
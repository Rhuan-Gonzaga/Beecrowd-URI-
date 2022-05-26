'''
1067 - Números Ímpares
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, 
um valor por linha, inclusive o X, se for o caso.

Entrada
O arquivo de entrada contém 1 valor inteiro qualquer.

Saída
Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.
'''
x = int(input())

if 1 <= x <=1000:
    for i in range(x + 1):
        if i % 2 == 1:
          print(i)
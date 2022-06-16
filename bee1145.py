"""
1145 - Sequencia logica 2
Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando para a próxima linha a cada X números.

Entrada
O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).

Saída
Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco entre cada número, 
conforme exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.

"""


x,y = map(int,input().split())

n = []
i = 0
k = 0
while i < y-x:
    for j in range(1, x + 1):
        n.append(i + 1)
        aux = n[k]
        n[k] = str(n[k])
        k = k + 1
        i = i + 1
   
    k = 0
    n = ' '.join(n)
    print(n)
    n =[]
z = y%x

if z ==0:
    for w in range(y - x,y):
        n.append(w + 1)
        n[k] = str(n[k])
        k = k + 1
    n = ' '.join(n)
    print(n)
if z !=0:
    for w in range(aux,y):
        n.append(w + 1)
        n[k] = str(n[k])
        k = k + 1
    n = ' '.join(n)
    print(n)
   
    
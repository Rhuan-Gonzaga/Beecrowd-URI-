'''
1133 - Resto da divisão
Escreva um programa que leia 2 valores X e Y e que imprima todos os 
valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, 
não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

'''
X = int(input())
Y = int(input())

if Y < X:
    #aux recebe o maior
    aux = X
    #X recebe Y,o menor
    X = Y
    #Y recebe o maior
    Y = aux

for i in range(X+1,Y):
    if i%5==2 or i%5==3:
        print(i)

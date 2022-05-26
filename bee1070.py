'''
1070 - seis numeros impares
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, 
um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.
'''
x=int(input())
cont=0
while cont<6:
    if x%2==1:
        print(x)
        cont+=1
    x+=1
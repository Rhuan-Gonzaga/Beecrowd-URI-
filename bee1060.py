'''
1060 - Numeros positivos
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). 
A seguir, mostre a quantidade de valores positivos digitados.

'''
contador = 0
for i in range(1,7):
    valor = float(input())
    if valor > 0:
        contador +=1
    
    
print('{} valores positivos'.format(contador))
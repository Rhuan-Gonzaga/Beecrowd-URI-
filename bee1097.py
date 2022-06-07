'''
1097 - Sequencia IJ 3
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo

'''
i = 1
j = 7

while i <= 9:
    for c in range(1,4):
        print('I={} J={}'.format(i,j))
        j = j - 1
    i = i + 2
    j = j + 5
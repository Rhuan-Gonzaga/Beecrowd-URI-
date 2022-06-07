'''
1096 - Sequencia IJ 2
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo
'''
count = 0
i = 1
j = 7
while count < 5:
    for n in range(3):
        print(f"I={i} J={j}")
        j-=1
    j=7
    i+=2
    count+=1

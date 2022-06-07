'''
1095 - Sequencia IJ 1
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo

'''
i = 1
j = 60
count = 0 

while count != j:
    print(f"I={i} J={j}")
    j-=5
    i+=3
print(f"I={i} J={j}")
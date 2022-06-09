'''
1115 - Quadrante
Escreva um programa para ler as coordenadas (X,Y) de uma 
quantidade indeterminada de pontos no sistema cartesiano. 
Para cada ponto escrever o quadrante a que ele pertence. 
O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA
(nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a 
coordenada lida, conforme o exemplo.
'''

while True:
    valores = [int(num) for num in input().split()]
    v1 = valores[0]
    v2 = valores[1]
    
    #primeiro (+,+)
    if v1 > 0 and v2 > 0:
        print("primeiro")
    #segundo (-,+)
    elif v1 < 0 and v2 > 0:
        print("segundo")
    #terceiro (-,-)
    elif v1 < 0 and v2 < 0:
        print("terceiro")
    #quarto (+,-)
    elif v1 > 0 and v2 < 0:
        print("quarto")
    else:
        break
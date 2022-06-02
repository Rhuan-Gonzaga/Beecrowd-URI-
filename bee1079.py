"""
1079 - Medias ponderadas
Leia 1 valor inteiro N, que representa o número de casos de teste que vem a 
seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma
casa decimal. Apresente a média ponderada para cada um destes conjuntos de 
3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o 
terceiro valor tem peso 5.

Entrada
O arquivo de entrada contém um valor inteiro N na primeira linha. 
Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

Saída
Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.


"""

conju_media = []
n = int(input())
count = 0

while count < n:
    valores = list(map(float,input().split()))
    media = (valores[0]*2 + valores[1]*3 + valores[2]*5)/10
    conju_media.append(media)
    count +=1
    
for i in conju_media:
    print(f"{i:.1f}")
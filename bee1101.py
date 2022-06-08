'''
1101 - Sequencia de Numeros e Soma
Leia um conjunto não determinado de pares de valores M e N 
(parar quando algum dos valores for menor ou igual a zero). 
Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros 
consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. 
A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles,
conforme exemplo abaixo.

'''
while True:
    valores = [int(x) for x in input().split()]
    m = min(valores)
    n = max(valores)
    
    if m <= 0:
        break
    
    texto = ""
    soma = 0
    for i in range(m, n+1):
        soma += i
        texto += str(i) + " "
    print("{}Sum={}".format(texto, soma))
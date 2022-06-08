'''
1099 - Soma de Ímpares Consecutivos II
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos 
os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste 
que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.

'''

n = int(input())

for n in range(n):
    linha = [int(num) for num in input().split()]
    x = min(linha)
    y = max(linha)
    
    soma = 0
    for num in range(x+1,y):
        if num % 2 == 1:
            soma += num
    print(soma)

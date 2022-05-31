'''
1073 - quadrado de pares
Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, 
de 1 até N, inclusive N, se for o caso.

Entrada
A entrada contém um valor inteiro N (5 < N < 2000).

Saída
Imprima o quadrado de cada um dos valores pares, de 1 até N, 
conforme o exemplo abaixo.

Tome cuidado! Algumas linguagens tem por padrão apresentarem como 
saída 1e+006 ao invés de 1000000 o que ocasionará resposta errada. 
Neste caso, configure a precisão adequadamente para que isso não ocorra.
'''
contador = 0
n = int(input())

if 5 < n < 2000:
    while contador < n:
        contador +=1
        if contador % 2 == 0:
            print(f"{contador}^2 = {contador**2}")
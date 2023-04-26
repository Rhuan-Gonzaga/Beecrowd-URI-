"""
1157 - Divisores I
Ler um número inteiro N e calcular todos os seus divisores

ENTRADA
O arquivo de entrada contém um valor inteiro

SAÍDA
Escreva todos os divisores positivos de N, um valor por linha

"""

n = int(input(""))
count  = 1
while count <= n:
    if n % count == 0:
        print(count)
    count +=1
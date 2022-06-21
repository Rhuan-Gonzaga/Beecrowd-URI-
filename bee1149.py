'''
1149 - Somando inteiros consecutivos
Faça um algoritmo para ler um valor A e um valor N. 
Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). 
Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

Entrada
A entrada contém somente valores inteiros, podendo ser positivos ou negativos.
Todos os valores estão na mesma linha.

Saída
A saída contém apenas um valor inteiro.

'''

x = list(map(int, input().split()))
i = 1
s = 0

while x[i] <= 0:
    if x[i] <=0:
        i = i + 1
    if x[i] > 0:
        break

for c in range(0,x[i]):
    s = s + x[0] + c
   
print(s)
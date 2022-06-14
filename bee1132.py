"""
1132 - Multiplos de 13
Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, 
incluindo ambos.

Entrada
O arquivo de entrada contém 2 valores inteiros quaisquer, 
não necessariamente em ordem crescente.

Saída
Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, 
inclusive ambos se for o caso

"""

x = int(input())
y= int(input())

if x > y:
    a = y
    b = x
if x <= y:
    a = x
    b = y
   
soma = 0


while a <= b:
    if a % 13 != 0:
        soma = soma + a
    a = a + 1
print(soma)

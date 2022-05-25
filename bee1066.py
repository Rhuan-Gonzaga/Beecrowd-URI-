'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, 
quantos valores digitados foram ímpares, quantos valores digitados foram 
positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, 
não esquecendo o final de linha após cada uma.
'''

contador_par = 0
contador_impa = 0
contador_posi = 0
contador_nega = 0


for i in range(5):
    valor = int(input())
    if valor % 2 == 0:
        contador_par += 1
    if valor % 2 == 1:
        contador_impa += 1
    if valor > 0:
        contador_posi += 1
    if valor < 0:
        contador_nega += 1

print(f"{contador_par} valor(es) par(es)")
print(f"{contador_impa} valor(es) impar(es)")
print(f"{contador_posi} valor(es) positivo(s)")
print(f"{contador_nega} valor(es) negativo(s)")
'''
1042 - Sort Simples

Leia 3 valores inteiros e ordene-os em ordem crescente. 
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, 
os valores na sequência como foram lidos.

'''

n1,n2,n3 = map(int,input().split())

lista = [n1,n2,n3]
lista2 = sorted(lista)

for i in range(len(lista)):
    print(lista2[i])

print() #Espaço em branco

for i in range(len(lista2)):
    print(lista[i])

    
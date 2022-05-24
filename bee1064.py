'''
1064 - positivos e media
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. 
Na próxima linha, 
deve-se mostrar a média de todos os valores positivos digitados, 
com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante.
Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. 
A próxima linha deve mostrar a média dos valores positivos digitados.

'''
contador =0
valor=0
for i in range(6):
    numero = float(input())
    if numero > 0:
        valor += numero
        contador +=1
        
print(f"{contador} valores positivos")
print("{:.1f}".format(valor/contador))

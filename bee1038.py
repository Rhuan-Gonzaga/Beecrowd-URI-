"""
1038 - Lanche

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

CODIGO      ESPECIFICAÇÃO         PREÇO
1           Cachorro Quente       R$4.00
2           X-Salada              R$4.50
3           X-Bacon               R$5.00
4           Torrada Simples       R$2.00
5           Refrigerante          R$1.50

"""

items = {1: 4.00 ,2: 4.50 ,3: 5.00 ,4: 2.00 ,5: 1.50}
A,B = map(int,input().split())
total = items[A] * B
print("Total: R$ %.2f" % total)
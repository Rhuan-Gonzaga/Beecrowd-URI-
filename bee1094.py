'''
1094 - Experiencias 
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

'''

n = int(input())
rato = 0
sapo = 0
coelho = 0
total_coba = 0

for i in range(n):
    quantia,tipo = input().split()
    if tipo == "C":
        coelho = coelho + int(quantia)
    if tipo == "S":
        sapo = sapo + int(quantia)
    if tipo == "R":
        rato = rato + int(quantia)
        
total_coba = (rato+sapo+coelho)
print(f"Total: {total_coba} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {100*coelho/total_coba:.2f} %")
print(f"Percentual de ratos: {100*rato/total_coba:.2f} %")
print(f"Percentual de sapos: {100*sapo/total_coba:.2f} %")

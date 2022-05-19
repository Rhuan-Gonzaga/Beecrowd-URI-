"""
Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, 
pois sabem que nele não existem
políticos corruptos e os recursos arrecadados são utilizados em benefício da população, 
sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. 
Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, 
segundo a tabela abaixo.

Renda                               Imposto de Renda
de 0.00 a R$ 2000.00                Isento
de R$ 2000.01 até R$ 3000.00        8%
de R$ 3000.01 até R$ 4500.00        18%
acima de R$ 4500.00                 28%

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, 
pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. 
No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, 
o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.
"""
a = float(input())

if(0<a<=2000):
    print("Isento")
elif(2000<a<=3000):
    t= (a-2000)
    tx= (t*8)/100
    print("R$ %.2f"%tx)
elif(3000<a<=4500):
    t= (a-2000)
    t1=t-1000
    tx1=(1000*8)/100
    tx2= (t1*18)/100
    print("R$ %.2f"%(tx1+tx2))
else:
    t= (a-2000)
    t1= t-1000
    tx1= (1000*8)/100
    t2=t1-1500
    tx2=(1500*18)/100
    tx= (t2*28)/100
    print("R$ %.2f" %(tx+tx1+tx2))
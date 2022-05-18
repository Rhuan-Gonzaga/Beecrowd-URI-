'''

A empresa ABC resolveu conceder um aumento de salários a seus 
funcionários de acordo com a tabela abaixo:

    Salario                 Percentual de Reajuste
    0 - 400.00                      15%
    400.01 - 800.00                 12%
    800.01 - 1200.00                10%
    1200.01 - 2000.00               7%
    Acima de 2000.00                4%                          
                                    
Leia o salário do funcionário e calcule e mostre o novo salário, bem como o
valor de reajuste ganho e o índice reajustado, em percentual.                                    
'''

salario = float(input())
percentual = 4

if (salario >= 0 and salario <= 400.00):
    percentual = 15
    porcentagem = (percentual/100) * salario
    total_salario = salario + porcentagem
    print("Novo salario: %.2f" % total_salario)
    print("Reajuste ganho: %.2f" % porcentagem)
    print(f"Em percentual: {percentual} %")
    
elif (salario >= 400.01 and salario <= 800.00):
    percentual = 12
    porcentagem = (percentual/100) * salario
    total_salario = salario + porcentagem
    print("Novo salario: %.2f" % total_salario)
    print("Reajuste ganho: %.2f" % porcentagem)
    print(f"Em percentual: {percentual} %")
   
elif (salario >= 800.01 and salario <= 1200.00):
    percentual = 10
    porcentagem = (percentual/100) * salario
    total_salario = salario + porcentagem
    print("Novo salario: %.2f" % total_salario)
    print("Reajuste ganho: %.2f" % porcentagem)
    print(f"Em percentual: {percentual} %")
    
elif (salario >= 1200.01 and salario <= 2000.00):
    percentual = 7
    porcentagem = (percentual/100) * salario
    total_salario = salario + porcentagem
    print("Novo salario: %.2f" % total_salario)
    print("Reajuste ganho: %.2f" % porcentagem)
    print(f"Em percentual: {percentual} %")
    
else:
    porcentagem = (percentual/100) * salario
    total_salario = salario + porcentagem
    print("Novo salario: %.2f" % total_salario)
    print("Reajuste ganho: %.2f" % porcentagem)
    print(f"Em percentual: {percentual} %")
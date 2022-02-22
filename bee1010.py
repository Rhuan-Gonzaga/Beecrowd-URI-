entrada_1, entrada_2 = input().split(), input().split()

quantidade_1 = int(entrada_1[1])
valor_1 = float(entrada_1[2])

quantidade_2 = int(entrada_2[1])
valor_2 = float(entrada_2[2])

total_1 = quantidade_1 * valor_1
total_2 = quantidade_2 * valor_2

total_pagar = total_1 + total_2
print('VALOR A PAGAR: R$ %.2f' %total_pagar)

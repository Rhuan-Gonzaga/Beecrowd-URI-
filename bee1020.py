valor = int(input(""))

ano = (valor//365)
mes = valor % 365//30
dia = valor % 365 % 30

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dia))
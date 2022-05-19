"""
1050 - DDD
Em seguida, informe à qual cidade o DDD pertence, 
considerando a tabela abaixo

    DDD         Destination
    61          Brasilia
    71          Salvador
    11          Sao Paulo
    21          Rio de Janeiro
    32          Juiz de Fora
    19          Campinas
    27          Vitoria
    31          Belo Horizonte
"""
codigo = int(input())
DDD = {61: "Brasilia", 71: "Salvador", 11: "Sao Paulo", 21: "Rio de Janeiro", 32: "Juiz de Fora",19: "Campinas", 27: "Vitoria", 31: "Belo Horizonte"}

if codigo in DDD:
    print(DDD[codigo])
else:
    print("DDD nao cadastrado")
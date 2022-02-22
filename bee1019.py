valor = int(input(""))

horas = (valor//3600)
minutos = (valor - (horas*3600)) //60
segundos = (valor % 60)

print("{}:{}:{}".format(horas, minutos, segundos))


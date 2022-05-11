"""
1035 - Teste de Seleção 1

Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

"""
A,B,C,D = map(int,input().split())

soma1 = C+D 
soma2 = A+B 

if B > C and D > A and soma1 > soma2 and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
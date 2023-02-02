"""Leia um valor N. Calcule e escreva seu fatorial correspondente. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro correspondente ao fatorial de N."""


def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero - 1)
    """
    Sequencia do codigo fatorial de numero 5: 

    1° chamada 5 * (5 -1 = 4)  |  2 * 1 = 2
    2° chamada 4 * (4 -1 = 3)  |  3 * 2 = 2
    3°chamada 3 * (3 - 1 = 2)  |  4 * 6 = 24
    4° chamada 2 * (2 - 1 = 1) |  5 * 24 = 120
    """

numero = int(input(""))
print(fatorial(numero))



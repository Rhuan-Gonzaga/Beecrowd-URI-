

"""
1047 - tempo de jogo com minutod
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
"""
hora_inicial,minuto_inicial,hora_final,minuto_final = map(int,input().split())

hora_total = hora_final - hora_inicial
if hora_total < 0:
    hora_total += 24


minuto_total = minuto_final - minuto_inicial
if minuto_total < 0:
    minuto_total += 60
    hora_total -= 1
    if hora_total < 0:
        hora_total += 24
    
if minuto_total == 0 and hora_total == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print(f"O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)")
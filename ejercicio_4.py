partidos_ganados=int(input('ingrese cantidad de partidos ganados: '))
partidos_perdidos=int(input('ingrese cantidad de partidos perdidos: '))
partidos_empatados=int(input('ingrese cantidad de partidos empatados: '))

puntaje_pg=partidos_ganados*3
puntaje_pe=partidos_perdidos*0
puntaje_pp=partidos_empatados*1

puntaje_total=puntaje_pg+puntaje_pe+puntaje_pp

print(puntaje_total)
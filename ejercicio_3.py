respuestas_correctas = int(input('Ingrese la cantidad de respuestas correctas :'))
respuestas_incorrectas = int(input('Ingrese la cantidad de respuestas incorrectas :'))
respuestas_blanco = int(input('Ingrese la cantidad de respuestas en blanco: '))

puntaje_rc = respuestas_correctas*3
puntaje_ri = respuestas_incorrectas*-1
puntaje_rb = respuestas_blanco*0

puntaje_final = puntaje_rc + puntaje_ri + puntaje_rb

print(f'puntaje final {puntaje_final}')
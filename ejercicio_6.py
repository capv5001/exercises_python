AX = int(input('ingrese coordendada del punto a en el eje X: '))
AY = int(input('ingrese coordendada del punto a en el eje Y: '))
BX = int(input('ingrese coordendada del punto b en el eje X: '))
BY = int(input('ingrese coordendada del punto b en el eje Y: '))

distancia = ((AX-BX)**2 + (AY-BY)**2)**0.5

print(distancia)
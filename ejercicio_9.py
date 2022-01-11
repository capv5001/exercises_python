litros_por_galon = 3.785
precio_por_litro = 4.50

cantidad_surtida = float(input('ingrese la cantidad surtida (galones):'))

total_a_pagar = litros_por_galon * precio_por_litro * cantidad_surtida


print(total_a_pagar)
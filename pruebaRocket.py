rocketCode= 0x1F680
rocket = chr(rocketCode)
print(rocket)

# La funcion chr() permite representar un carácter a partir de su código:

#La función ord() permite obtener el código (decimal) de un carácter a partir de su representación:
rocket_code = hex(ord(rocket))
print(rocket_code)

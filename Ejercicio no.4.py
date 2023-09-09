numero_telefono = input("Bienvenido, por favor Ingrese un número de teléfono en formato +34-: ")

componentes = numero_telefono.split('-')

if len(componentes) == 3 and componentes[0] == '+34' and len(componentes[1]) == 9 and len(componentes[2]) == 2:
    numero_central = componentes[1]
    
    print("El número de teléfono sin el prefijo y la extensión es:", numero_central)
else:
    print("El formato del número de teléfono no es válido.")
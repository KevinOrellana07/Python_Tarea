correo_original = input("Bienvenido, por favor, ingresa tu correo electrónico: ")

nombre, dominio = correo_original.split('@')

nuevo_correo = f"{nombre}@ceu.es"

print("Nuevo correo electrónico:", nuevo_correo)
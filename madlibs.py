# Concaternar cadenas de caracteres
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con __________.

# organizacion = "OpenBootcamp"

# print("Aprendo a programar con " + organizacion)
# print("Aprendo a programar con {}".format(organizacion))
# print(f"Aprende a programar con {organizacion}") #f-string

adj = input("Adjetivo: ")
verbo1 = input("Verbo1: ")
verbo2 = input("Verbo2: ")
sustantivo_prural = input("Sustantivo (prural): ")


madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprendo a {verbo2} en mi freecodecamp y así alcanzar mis {sustantivo_prural}!"

print(madlib)

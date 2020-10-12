


import math

print("-------------------------------------------------------------------")
print("                      Ejercicio 4")
print("-------------------------------------------------------------------")
print("                      Bienvenido a tu calculadora de Gigas")
print(" ")
print("Primero indicame el tamaño de tu copia de seguridad en Gigabytes ")
while True:
        try:
            
            gigas = float(input())
        except ValueError:
            print("Debes escribir un número.")
            print("indicame el tamaño de tu copia de seguridad en Gigabytes ")
            continue

        if gigas <= 0:
            print("Debes escribir un número positivo.")
            print("indicame el tamaño de tu copia de seguridad en Gigabytes ")
            continue
        else:
            break

gb= gigas * 1024
print(" ")
print("en Megabytes, eso es: ", gb, "MB")
cds= gb / 700
input()
print(" ")
print("necesitas un estimado de:", math.ceil(cds), "Cd's")
print(" ")
input()
print(" ¡Gracias por usar este Servicio!")

print("fin.")

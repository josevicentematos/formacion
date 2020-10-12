promediom = 0
promedioa = 0
promediov = 0

contm, contv, conta, ct= 0, 0, 0, 0

a, v, m = 0, 0, 0
print("-------------------------------------------------------------------")
print("                      Ejercicio 5")
print("-------------------------------------------------------------------")
while ct < 20f
:
    while True:
        try:
            print ("Introduzca la edad de la persona: ")
            edad = int(input())
        except ValueError:
            print("Debes escribir un número.")
            continue

        if edad <= 0:
            print("Debes escribir un número positivo.")
            continue
        else:
            break
    if edad <= 18:
        a = a + 1
        conta = conta + edad
        
    elif edad >= 60:
        v = v + 1
        contv = contv + edad

    else:
        m = m + 1
        contm = contm + edad
    ct = ct + 1

if a != 0:
    promedioa = conta / a
    print ("Promedio de la edad de las personas menores de edad es:",int(promedioa))
else:
    print("no se consultaron personas adultas ")
    
if m != 0:
    promediom = contm / m
    print ("Promedio de la edad de los adultos es:",int(promediom))

else:
    print("no se consultaron personas menores de edad ")

if v != 0:
    promediov = contv / v
    print ("Promedio de la edad de los adultos mayores es:",int(promediov))
else:
    print("no se consultaron adultos mayores ")

print("personas consultadas:",ct)



print("Fin.")



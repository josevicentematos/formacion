print("-------------------------------------------------------------")
print("            Ejercicio 3")
print("-------------------------------------------------------------")


lista = []
for x in range(5):
    print("Ingrese valor:")
    while True:
        try:
            
            valor = int(input())
        except ValueError:
            print("Debes escribir un número.")
            print("ingresa un valor permitido")
            continue

        if valor <= 0:
            print("Debes escribir un número positivo.")
            print("ingresa un valor permitido ")
            continue
        else:
            break
            
    lista.append(valor)

menor = lista[0]
auxp = 0
for x in range(1,5):
    if lista[x] < menor:
        menor = lista[x]
        auxp = x + 1

auxc = 0
for x in range(5):
    if menor == lista[x]:
        auxc = auxc +1
       
            

print("Lista completa")
print(lista)
print("Numero menor de la lista")
print(menor)
if auxc > 1:
    print("el elemento se repite en las siguientes posiciones")
    auxp = 0
    for x in range(5):
        if lista[x] == menor:
            auxp = x + 1
            print("Posicion:", auxp)

print("Fin.")

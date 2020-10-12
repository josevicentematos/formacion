print("-------------------------------------------------------------")
print("                Ejercicio 3.1")
print("-------------------------------------------------------------")


lista = []
if lista:
    print("no vacio")

else:
    print("Creando nueva lista...")
    print("Ingrese valor: (pulsa 0 para terminar)")
    valor = int(input())
    if valor > 0:
        lista.append(valor)
        
    while valor > 0:
        print("Ingrese valor: (pulsa 0 para terminar)")
        while True:
            try:
            
                valor = int(input())
            except ValueError:
                print("Debes escribir un número.")
                print("ingresa un valor permitido (pulsa 0 para terminar)")
                continue

            if valor <= -1:
                print("Debes escribir un número positivo.")
                print("ingresa un valor permitido (pulsa 0 para terminar)")
                continue
            else:
                break
        if valor > 0:
            lista.append(valor)
aux = len(lista)
print("la lista es:", lista)

menor = lista[0]
auxp = 0
for x in range(1,aux):
    if lista[x] < menor:
        menor = lista[x]
        auxp = x + 1

auxc = 0
for x in range(aux):
    if menor == lista[x]:
        auxc = auxc +1
       
print("Numero menor de la lista")
print(menor)
if auxc > 1:
    print("el elemento se repite en las siguientes posiciones")
    auxp = 0
    for x in range(aux):
        if lista[x] == menor:
            auxp = x + 1
            print("Posicion:", auxp)




print("Fin.")

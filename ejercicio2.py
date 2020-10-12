
from datetime import datetime, date, time, timedelta

print("-------------------------------------------------------------------")
print("                      Ejercicio 2")
print("-------------------------------------------------------------------")
print("               Datos de carrera       ")
print(" ")
print("nombre del primer corredor")   
n1 = input()
print("indica el tiempo de este corredor, Horas:Minutos:Segundos")
hora1 = (input())
print("nombre del segundo corredor")
n2 = input()
print("indica el tiempo de este corredor, Horas:Minutos:Segundos")
hora2 = (input())

format_hora = "%H:%M:%S"

h1 = datetime.strptime(hora1, format_hora)
h2 = datetime.strptime(hora2, format_hora)

totalhoras = h1 - h2
print("hora del primer corredor" + hora1)
print("hora de segundo corredor" + hora2)

def sumar_hora(ho1,ho2):#paso de parametros 
    formato = "%H:%M:%S"
    lista = ho2.split(":")#conviert la hora en lista  
    hora=int(lista[0]) #enlisto hora
    minuto=int(lista[1]) #enlisto minuto
    segundo=int(lista[2]) #enlisto segundos 
    h1 = datetime.strptime(ho1, formato)#aqui se mete en hora1
    dh = timedelta(hours=hora)  #agrega con time delta hora1
    dm = timedelta(minutes=minuto)    #agrega con time delta minutos1       
    ds = timedelta(seconds=segundo)  #agrega con time delta segundos1
    resultado1 =h1 + ds #suma a estilo tiempo segundos de ho2 a ho1
    resultado2 = resultado1 + dm #suma a estilo tiempo minutos de ho2 a ho1
    resultado = resultado2 + dh #suma a estilo tiempo horas de ho2 a ho1
    resultado=resultado.strftime(formato)#agrega el formato inicial a esas sumas
    return str(resultado) #devuelve el valor 

print("la suma de los dos tiempos es:")
print(sumar_hora(hora1,hora2))

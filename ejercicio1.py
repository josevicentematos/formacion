print("-------------------------------------")
print("Ejercicio N°1")

palabra  = input("escribe una palabra: ")
if palabra.isalpha():
      
    if str(palabra) == str(palabra)[::-1]:
        print("esta palabra es Palindroma")
        print(">>", palabra)
        print("<<", palabra[::-1])
    else:
        print("como ves, esta palabra no es Palindroma")
        print(">>", palabra)
        print("<<", palabra[::-1])

else:
  print("La tiene caracteres que no son del alfabeto")

print("esta palabra contiene:" ,len(palabra),"letras")

print("fin.")
    

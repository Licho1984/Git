
calificacion = 85

if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")



frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)


contador = 0
while contador < 5:
    print(contador)
    contador += 1  

contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break      
    
frutas = ["manzana", "banana", "naranja"]
print(frutas[0])
print(frutas[1])
print(frutas[2])
frutas.append("kiwi")
print(frutas)

punto = (3, 4)
##print(punto[0])
print(punto[1])
  


mi_tupla = (1, 2, 3, 2, 4, 2)
print (mi_tupla.index(2))   # Salida: 1
print (mi_tupla.index(2, 2))   #Salida: 3
print (mi_tupla.index(2, 2, 4))   #Salida: 3


persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])

persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}



frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])
print(frutas)
print(numeros)
print(type(frutas))
print(type(numeros))


conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}
interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}
diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}



frutas = {"manzana", "banana", "naranja"}
frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}
frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}
frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}
frutas.clear()
print(frutas)  # Imprime set()
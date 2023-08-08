millista=["apple", "banana", "cherry", "orange", "kiwi", "melon","mango"]
print(millista[-4:-1])

if "apple" in millista:
    print("Yes")

millista[1:3]= ["blackcurrant", "watermelon"]
print(millista)

#PARA INSERTAR EN DETERMINADO INDEX QUE SE DA EN EL PRINCIPIO, arrastrando el dato que se encuentre ahí al sgte index'
millista.insert(5, "watermelon")
print(millista)

#PARA AGRGAR EN LO ULTIMO COMO UNA COLA'
millista.append("orange")
print(millista)

tropical=["mango", "pineapple", "papaya"]
millista.extend(tropical)
print(millista)

#PARA ELIMINAR SEGUN EL NOMBRE, el primero que encuentre'
millista.remove("mango")
print(millista)

#PARA ELIMINAR SEGÚN EL INDEX QUE QUIERAS, si no se coloca el index elimina el ultimo elemento'
millista.pop(1)
print(millista)



#RECORER LA LISTA'

#for x  in millista:'
#    print(x)'

#Lo mismo de lo anterior pero en una sola linea'
[print(x) for x in millista]

#i=0'
#while i < len(millista):'
#    print(millista[i])'
#    i += 1'



#PARA ESCOGER LAS PALABRAS QUE TENGAN LA LETRA EN LA LISTA'
newlist = [x for x in millista if "a" in x]
print("AQUI ... ", newlist)





#----------------------------------------------------------------------------------------------------------------------------





#DICCIONARIO'
thisdict={
    "brand":"Ford",
    "model":"Muntang",
    "year":1925,
    "dueños":["Samuel", "Jefferson", "Maria", "Rosa"]
}

print(thisdict["dueños"])
print(len(thisdict))

#imprmirmir la claves del diccionario'
print(thisdict.keys())
print(thisdict.get("year"))

#CAMBIAR VALOR A CLAVE EXISTENTE'
thisdict["year"]=2023

print(thisdict.values())

#AGREGAR CLAVE CON VALOR'
thisdict["color"]="Rojo lava"
print(thisdict)

#BORRAR CLAVE CON SU VALOR
del thisdict["color"]
print(thisdict)

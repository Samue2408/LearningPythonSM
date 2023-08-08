#SAMUEL MALDONADO MONTERO

x= int(input("Cuantas categorias va a ingresar"))

Categorias = {}

for n in range(x):

    id = input("ID de la categoria ")
    nom = input("Nombre de la categoria ")
    print("")

    Categorias[n+1]={"id":id,"nombre":nom}

print(Categorias)

producto = {}

x= int(input("¿Cuantos productos va a ingresar?"))

for c in range(x):
    
    id = input("ID del producto ")
    nom = input("Nombre del producto ")
    precio = input("Precio del producto ")
    id_cat = input("Id de la categoria del producto ")
    print("")

    producto1={"Id":id,"Nombre":nom, "Precio":precio, "Id cat":id_cat}
    producto [c+1]=producto1

print(producto)

DiccionarioResultante = {}

for d in range(len(producto)):
    for f in range(len(Categorias)):
        if producto[d+1]["Id cat"] in Categorias[f+1]["id"]:
            id = producto[d+1]["Id"] 
            nombp = producto[d+1]["Nombre"]
            nombc = Categorias[f+1]["nombre"]

            DiccionarioResultante[d+1]={"Id":id, "Nombre producto":nombp, "Nombre categoria":nombc}

print(DiccionarioResultante)  

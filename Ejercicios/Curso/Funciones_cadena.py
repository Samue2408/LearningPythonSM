texto = "Bienvenido al programa de Samuel Maldonado"

print(texto)
print(texto.lower()) #todos los caracteres en minuscula
print(texto.upper()) #todos los caracteres en mayuscula
print(texto.title()) #La letras iniciales se ponen en mayuscula

print(texto.find("al")) #nos dice la posicion en la que se encuentra la palabra ingresada, si no se encuentra dice -1

print(texto.count("e")) #contar cuantas veces se repite el caracter indicado

textofinal = texto.replace("e","3") #remplazar algun caracter por otro
print(textofinal)

valor = texto.isnumeric() #saber si es una variable numerica, existen muchas mas, se pueden ver colocando .is***
print(valor)

cadenaSeparada = texto.split(" ")#para separar mediante un parametro una cadena de texto en diferentes componentes
print(cadenaSeparada)




'''
Strings and arrays
'''

a = "hola, mundo"
print(a[2])

for x in "banana":
    print(x)

a = "hello, world"
print(len(a))

txt = "the best things in life are free"
print("free" in txt)

txt = "the best things in life are free"
if "free" in txt:
    print("yes,  'free' is present")

txt  = "the best things in life are free"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")

txt = "the best things in life are free"
print("expensive" not in txt)

b = " Hello, World! "
print(b[2:5])

print(b[:5])

print(b[2:])

print(b[-5:-2])

print(b.upper())

print(b.lower())

print(b.strip()) #returns "Hello, World!" , quiere decir que borra los espacios que tienen las cadenas de textos

print(b.replace("H", "j"))

print(b.split(",")) #returns ['Hello', 'World']

age = 20
txt = "my name is cesar, i am " + str(age)
print(txt)

txt = "my name is cesar, and i am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "i want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

myorder = "i want to pay  {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))
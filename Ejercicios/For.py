# equivalente a un while con un contador
for x in range(10):
    print("valor de x: ", x)

# x va a tomar valores desde el 10 hasta el 29
for x in range(10, 30):
    print("valor de x: ", x)

# x va a tomar valores desde el 20 hasta el 29 de 2 en 2
for x in range(20, 30, 2):
    print("valor de x: ", x)

# x toma el valor de cada caracter del String
for x in "Python":
    print(x)

# El end es para que el print no haga salto de linea
# for x in 'Python hi':
#    print(x, end='')

# Control del signo @
arroba = "@"
cantidad = 0
mail = input("Ingerse su email: ")
for x in mail:
    if x == arroba:
        cantidad += 1

if cantidad == 1:
    print("mail correcto")
else:
    print("mail incorrecto")

# Tabla de multiplicar
valor = int(input("Valor de la tabla"))
print("Eligio ver la tabla del: ", valor)
for x in range(11):
    print(x, " X ", valor, "= ", x * valor)

# Saber los numeros primos desde el 1 hasta el que usuario indique
pri = int(input("Ingrese hasta el numero que quiere saber si son primos"))

con = 0
for x in range(2, pri):
    c = 0
    for f in range(2, x):
        if x % f == 0:
            c = 1
            break
    if c == 0:
        con += 1
        print(x)


print("Hay ", con, " numeros primos del 1 al ", pri)

# La funcion "CONTINUE" hace que el ciclo continúe, dejando de hacer las instrucciones que siguen despues de esta funcion
# El uso de esta sentencia rompe la iteracion de dicho bucle.
# Provocando que se ejecute la siguiente iteracion de dicho bucle, ignorando las sentencias posteriores a "continue"
for letra in "Programecion":
    if letra == "e":
        print("Letra erronea")
        continue
    print(letra)

# La funcion "PASS" permite continuar con una sentencia o funcion que ya no tiene o aun no tinen un bloque de codigo util
# Es decir si se quiere dejar un if sin ninguna intruccion dentro de él
# Tambien sirve cuando no se le quiere poner instrucciones a una funcion

for numero in range(1, 6):
    if numero <= 3:
        # Aqui no pasa nada y el bucle sigue trabajando
        pass
    else:
        print("El siguiente valor es mayor a 3:")
    print("El numero es: {0}".format(numero))

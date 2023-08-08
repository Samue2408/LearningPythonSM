num1 = int(input("Ingrese el numero que quiere saber el factorial "))

i = 1
for x in range(1, num1+1):
    i = i * x

print("El factorial del numero {0} es: {1}".format(num1, i))
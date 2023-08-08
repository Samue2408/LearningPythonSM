# Excepcion: error en tiempo de ejecucion del programa

num1 = 20
num2 = 2

#print("La division de {0} entre {1} es: {2}".format(num1, num2, (num1/num2)))

try:
    resultado = num1 / num2

#except:
except ZeroDivisionError:
    print("No se puede dividir entre cero")

finally:#Siempre se va a ejecutar
    print("Yo siempre aparezco")

print("aqui termina")
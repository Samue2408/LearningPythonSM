#SAMUEL MALDONADO MONTERO

def menu(func):
    def wrapper():
        while True:
            print("\n=== CALCULADORA ===")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            print("5. Salir")
            opcion = int(input("Seleccione una opción: "))
            if opcion <5:
                numero1 = float(input("Ingrese el primer número: "))
                numero2 = float(input("Ingrese el segundo número: "))
                resultado = operacion(numero1, numero2, opcion=opcion)
                print("El resultado es:", resultado)
            elif opcion == 5:
                print("Salió")
                break
            else:
                print("Opción incorrecta")
            
    return wrapper

def operacion(*args, opcion):
    if opcion == 1:
        resultado =  args[0] + args[1]
    elif opcion == 2:
        resultado = args[0] - args[1]
    elif opcion == 3:
        resultado =  args[0] * args[1]
    elif opcion == 4:
        if args[1] == 0:
            resultado = None
            print("Error: No se puede dividir entre cero.")
        else:
            resultado =  args[0] / args[1]
    else:
        resultado = None
        print("Opción inválida")
    return resultado

@menu
def calcular(*args):
    return operacion(*args, opcion=args[-1])

calcular()


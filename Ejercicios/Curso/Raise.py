# Raise: Sirve para lanzar (de forma intencional) errores o excepciones en Python

def evaluarNota(nota):
    if nota < 0:
        raise ValueError("No se permiten valores negativos")
        #raise ZeroDivisionError("No se permiten valores negativos")
    elif nota >= 16:
        print("Excelente")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Desaprobado")
    
evaluarNota(-2)
    

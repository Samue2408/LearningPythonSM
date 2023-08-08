from datetime import datetime, timedelta, date, time

fecha = datetime.now()
"""
print(fecha)

fecha = datetime(2020, 11, 5)
print(fecha)

fecha = datetime(2020, 11, 5, 10, 35, 21)
print(fecha)
"""

"""
Los Formatos se pueden encontrar en este link "https://strftime.org/"
"""
# fechaActual = datetime.strftime(fecha, '%d/%m/%Y %H:%M:%S') # Para este formato dd/mm/YYYY HH:mm:ss
# print(fechaActual)

# fechaActual = datetime.strftime(fecha, '%b %d %Y %H:%M:%S') # Para este formato "Jul 10 2023 HH:mm:ss"
# print(fechaActual)

# FechaTexto = 'Dec 06 2020 12:56:11'
# fechaActual = datetime.strptime(FechaTexto,'%b %d %Y %H:%M:%S') #sirve para cambiar de formato un texto a formato datetime
# print(fechaActual)

#dia = datetime.strftime(fecha, "%d")
#print(dia)

#hora = datetime.strftime(fecha, "%H:%M")
#print(hora)


"""
fechaVieja = datetime(2023, 5, 19)
diferencia = fecha - fechaVieja

print(diferencia)
print(diferencia.days)
print(diferencia.total_seconds)
"""


"""
# Para sumar o restar dias
dia_delta = timedelta(days=5)# Si quieres restar se coloca el numero negativo
Fechainicial = date.today()
print(Fechainicial)
fechaFutura = Fechainicial + dia_delta
print(fechaFutura)
"""

#fecha = datetime.now().isoformat() # Formato para iso


def obtener_hora_ingresada():
    # Función para solicitar y obtener la hora y el minuto ingresados por el usuario.
    while True:
        try:
            hora = int(input("Ingresa la hora (0-23): "))
            minuto = int(input("Ingresa los minutos (0-59): "))
            if 0 <= hora <= 23 and 0 <= minuto <= 59:
                return hora, minuto
            else:
                print("Hora o minuto inválido. Intenta nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

# Preguntar al usuario si desea realizar la acción en el mismo instante o a una hora determinada
opcion = input("¿Deseas realizar la acción en el mismo instante? (Sí/No): ").lower()

if opcion.startswith("s"):
    # Acción en el mismo instante (obtener la hora actual)
    hora_actual = datetime.now().time()
    hora, minuto = hora_actual.hour, hora_actual.minute
else:
    # Acción a una hora determinada (solicitar la hora y el minuto al usuario)
    hora, minuto = obtener_hora_ingresada()

# Realizar la acción en un bucle "for" con incremento de un minuto en cada iteración
for _ in range(10):  # Cambiar 10 por la cantidad deseada de iteraciones
    # Hacer algo con las variables "hora" y "minuto"
    print(f"Realizando la acción a las {hora:02d}:{minuto:02d}")
    # Sumar un minuto para la próxima iteración
    nueva_hora = (datetime.combine(datetime.min, time(hora, minuto)) + timedelta(minutes=1)).time()
    hora, minuto = nueva_hora.hour, nueva_hora.minute


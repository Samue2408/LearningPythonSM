#SAMUEL MALDONADO MONTERO

tarifa = 0
horas = -1
minutos = -1
# Solicitar día de la semana
dia = input('Ingrese el día de la semana (primera letra en mayúscula): ')

if dia == 'Lunes' or dia == 'Martes' or dia == 'Miercoles':
    tarifa = 2.00
elif dia == 'Jueves' or dia == 'Viernes':
    tarifa = 2.50
elif dia == 'Sabado' or dia == 'Domingo':
    tarifa = 3.00
else:
    print ('Error: Día de la semana inválido')

# Verificar si el día ingresado es válido
if tarifa != 0:
    # Solicitar tiempo estacionado en horas y minutos
    horas = int(input('Ingrese las horas estacionado: '))
    minutos = int(input('Ingrese los minutos estacionado: '))
    
    if horas < 0 or minutos < 0:
        print('Error en el tiempo estacionado ingresado')
    else:
        # Verificar si la cantidad de minutos es mayor o igual a 5
        if minutos >= 5:
            horas += 1  # Redondear hacia arriba a la hora siguiente

        # Calcular costo total según las tarifas
        costo = horas * tarifa

        # Mostrar costo total
        print('El costo del estacionamiento es: $',costo)
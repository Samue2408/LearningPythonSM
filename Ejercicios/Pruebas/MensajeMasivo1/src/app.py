from tkinter import messagebox
import datetime
import pyautogui as pg
import pandas as pd
import pywhatkit
import time


file = "D:\SAMUEL\Python\Ejercicios\Pruebas\MensajeMasivo1\src\Clientes.xlsx"
data = pd.read_excel(file, sheet_name="Ventas")

opc = input("Desea mandar el mensaje en este instante? (y/n)")
if opc == "y":
    hora_actual = datetime.datetime.now().time()
    hora, minutos = hora_actual.hour, hora_actual.minute
else:
    while True:
        try:
            hora = int(input("Ingresa la hora (0-23): "))
            minutos = int(input("Ingresa los minutos (0-59): "))
            if 0 <= hora <= 23 and 0 <= minutos <= 59:
                break
            else:
                print("Hora o minuto inválido. Intenta nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

for i in range(len(data)):
    celular = data.loc[i, "Celular"].astype(
        str
    )  # Convertir a string para que se añada al mensaje
    nombre = data.loc[i, "Nombre"]
    producto = data.loc[i, "Producto"]

    # Crear mensaje personalizado
    message = (
        "Hola, " + nombre + "! Gracias por comprar " + producto + " con nosotros 🙌"
    )

    nueva_hora = (datetime.datetime.combine(datetime.datetime.min, datetime.time(hora, minutos)) + datetime.timedelta(minutes=1)).time()
    hora, minutos = nueva_hora.hour, nueva_hora.minute

    pywhatkit.sendwhatmsg("+57" + celular, message, hora, minutos, 10, True, 10)

    # Repetir el print 5 veces
    for _ in range(15):
        pg.press('tab')
    time.sleep(2)
    pg.press('enter')
    time.sleep(2)
    pg.hotkey("ctrl", "w")

messagebox.showinfo("Proceso Finalizado", "Se han enviado todos los mensajes")

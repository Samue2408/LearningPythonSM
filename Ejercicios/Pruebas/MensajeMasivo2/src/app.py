from tkinter import messagebox
import webbrowser as web
import pyautogui as pg
import pandas as pd
import pywhatkit
import time


file = "D:\SAMUEL\Python\Ejercicios\Pruebas\MensajeMasivo2\src\Clientes.xlsx"
data = pd.read_excel(file, sheet_name="Ventas")

opc = input("Desea mandar el mensaje en este instante? (y/n)")
if opc == "n":
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
elif opc == "y":
    pass
else:
    print("Opcion invalida")



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
    if opc == 'y':
        web.open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + message)
    else:
        pywhatkit.sendwhatmsg("+57" + celular, message, hora, minutos, 10, False, 10)
        opc = 'y'
        continue
    

    time.sleep(12)
    pg.click(924,733)
    time.sleep(2)
    pg.press('enter')
    time.sleep(4)
    pg.hotkey("ctrl", "w")

messagebox.showinfo("Proceso Finalizado", "Se han enviado todos los mensajes")

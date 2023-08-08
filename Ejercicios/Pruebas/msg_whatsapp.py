import pywhatkit

#Enviar mensajes automatizados por WhatsApp

number = input("Ingrese el numero de telefono")
message = input("Digite el mensaje que quiere enviar")
hour = int(input("Ingrese la hora a la que se quiere enviar"))
minutes = int(input("Ingrese los minutos"))

pywhatkit.sendwhatmsg("+57"+number, message, hour, minutes, 20, False, 10)
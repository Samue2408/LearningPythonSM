import random
from werkzeug.security import generate_password_hash
minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@()[]{}+,;/-_¿?.¡!$<#>&+%="

base = minus + mayus + numeros + simbolos
longitud = 12

for _ in range(10):
    muestra = random.sample(base, longitud)
    password = "".join(muestra)
    pass_encrip = generate_password_hash(password)
    print("{0} => {1}".format(password, pass_encrip))

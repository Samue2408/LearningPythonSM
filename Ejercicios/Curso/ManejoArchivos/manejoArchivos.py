
"""

'r': Solo lectura.
'w': Escritura (crea un archivo nuevo o sobrescribe uno existente).
'x': Creación exclusiva (falla si el archivo ya existe).
'a': Adición (escritura al final del archivo, crea un archivo nuevo si no existe).
'b': Modo binario (se puede combinar con cualquier otro modo para trabajar con archivos binarios).
't': Modo de texto (valor predeterminado, se puede combinar con cualquier otro modo para trabajar con archivos de texto).
'r+': Lectura y escritura.
'w+': Escritura y lectura (crea un archivo nuevo o sobrescribe uno existente).
'x+': Creación exclusiva para lectura y escritura.
'a+': Adición y lectura (escritura al final del archivo, crea un archivo nuevo si no existe).
'rb': Modo binario para lectura.
'wb': Modo binario para escritura (crea un archivo nuevo o sobrescribe uno existente).
'xb': Creación exclusiva en modo binario.
'ab': Adición en modo binario (escritura al final del archivo, crea un archivo nuevo si no existe).
'rt': Modo de texto para lectura (valor predeterminado).
'wt': Modo de texto para escritura (crea un archivo nuevo o sobrescribe uno existente).

"""

file = open('d:\SAMUEL\Python\Ejercicios\Curso\ManejoArchivos\data1.txt', 'r', encoding='utf-8') # El encodin es para los caracteres del idioma español
print(file)

lineas = file.readlines()
print(lineas) 

file.close()



with open('d:\SAMUEL\Python\Ejercicios\Curso\ManejoArchivos\data2.txt', 'r', encoding='utf-8') as archivo:  # el with se utiliza para darle un alias al archivo y con el with hay un cierre automatico en cuanto se terminen las instrucciones
    lineas = archivo.readlines()
    print(lineas)

for l in lineas:
    print(l, end='')



with open('d:\SAMUEL\Python\Ejercicios\Curso\ManejoArchivos\data2.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    lineas = contenido.split('\n')
    print(lineas)



with open('d:\SAMUEL\Python\Ejercicios\Curso\ManejoArchivos\data2.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    lineas = contenido.split('\n')
    pos = archivo.tell() # para saber la posicion en la que nos encontramos en el archivo
    print("el archivo tiene {0} caracteres de longitud".format(pos))



with open('d:\SAMUEL\Python\Ejercicios\Curso\ManejoArchivos\data2.txt', 'r', encoding='utf-8') as archivo:
    archivo.seek(7) # para iniciar el archivo desde determinada posicion de los caracteres
    pos = archivo.tell()
    print(pos)
    contenido = archivo.read()
    lineas = contenido.split('\n')
    print(lineas)



with open('d:\SAMUEL\Python\Ejercicios\Curso\ManejoArchivos\data2.txt', 'r', encoding='utf-8') as archivo:
    siguientes4 = archivo.read(7) # con los numeros se puede decidir cuantos caracteres a leer
    print(siguientes4)



with open('d:\SAMUEL\Python\Ejercicios\Curso\ManejoArchivos\data2.txt', 'rb') as archivo:
    print(type(archivo.read()))

with open('d:\SAMUEL\Python\Ejercicios\Curso\ManejoArchivos\data2.txt', 'r') as archivo:
    print(type(archivo.read()))

"""
with open('d:\SAMUEL\Python\Ejercicios\Curso\ManejoArchivos\data3.txt', 'w') as archivo:
    archivo.write("Oscar\nAlejandro\nSamuel")
"""

with open('d:\SAMUEL\Python\Ejercicios\Curso\ManejoArchivos\data3.txt', 'a') as archivo:
    archivo.write("\nSantiago\nEstaban")
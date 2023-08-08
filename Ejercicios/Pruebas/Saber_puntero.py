import tkinter as tk

def mostrar_coordenadas(event):
    # Mostrar las coordenadas del mouse en la etiqueta de la ventana
    coordenadas_label.config(text=f"X: {event.x}, Y: {event.y}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Posición del Mouse")

# Crear una etiqueta para mostrar las coordenadas
coordenadas_label = tk.Label(ventana, text="X: 0, Y: 0")
coordenadas_label.pack(padx=10, pady=5)

# Capturar el movimiento del mouse y llamar a la función mostrar_coordenadas
ventana.bind("<Motion>", mostrar_coordenadas)

# Iniciar el bucle principal
ventana.mainloop()

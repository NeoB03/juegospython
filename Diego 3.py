import tkinter as tk
import random
import tkinter.font as tkFont

# Generar el número secreto
numero_secreto = random.randint(0, 100)
puntuacion = 0

def verificar_numero():
    global puntuacion
    intento = int(entrada.get())
    if intento < numero_secreto:
        mensaje.set("El número es mayor ⬆")
    elif intento > numero_secreto:
        mensaje.set("El número es menor ⬇")
    else:
        mensaje.set("¡Felicidades! 🎉 Has adivinado el número.")
        mostrar_animacion()
        boton_reiniciar.pack()
        puntuacion += 1
        etiqueta_puntuacion.config(text=f"Puntuación: {puntuacion}")

def reiniciar_juego():
    global numero_secreto
    numero_secreto = random.randint(0, 100)
    mensaje.set("Intenta adivinar el número entre 0 y 100")
    entrada.delete(0, tk.END)
    animacion.place_forget()
    boton_reiniciar.pack_forget()

def mostrar_animacion():
    global animacion
    animacion = tk.Label(ventana, text="🎊🎈🎉", font=('Helvetica', 48), fg='orange')
    animacion.place(x=150, y=200)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Adivina el Número")
ventana.geometry("400x350")
ventana.configure(bg='#e1f5fe')

# Configurar fuentes
fuente_titulo = tkFont.Font(family="Helvetica", size=20, weight="bold")
fuente_mensaje = tkFont.Font(family="Helvetica", size=14)
fuente_boton = tkFont.Font(family="Helvetica", size=12, weight="bold")

# Widgets de la interfaz
tk.Label(ventana, text="Introduce un número del 0 al 100:", font=fuente_titulo, bg='#e1f5fe').pack()
entrada = tk.Entry(ventana, font=fuente_mensaje)
entrada.pack()
boton_verificar = tk.Button(ventana, text="Comprobar", font=fuente_boton, command=verificar_numero, bg='#80d8ff')
boton_verificar.pack(pady=10)
mensaje = tk.StringVar()
mensaje.set("Intenta adivinar el número entre 0 y 100")
etiqueta_mensaje = tk.Label(ventana, textvariable=mensaje, font=fuente_mensaje, bg='#e1f5fe')
etiqueta_mensaje.pack()

# Puntuación
etiqueta_puntuacion = tk.Label(ventana, text=f"Puntuación: {puntuacion}", font=fuente_mensaje, bg='#e1f5fe')
etiqueta_puntuacion.pack()

boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", font=fuente_boton, command=reiniciar_juego, bg='#ff8a80')

# Iniciar el bucle de eventos
ventana.mainloop()

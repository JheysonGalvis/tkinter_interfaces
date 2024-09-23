import tkinter as tk  # Importa la biblioteca tkinter y la renombra como tk para facilitar su uso.
ventana = tk.Tk()  # Crea una ventana principal de la aplicación.

ventana.title("Mi ventana")  # Establece el título de la ventana como "Mi ventana".
ventana.geometry("600x400")  # Define el tamaño de la ventana a 600 píxeles de ancho y 400 píxeles de alto.
ventana.configure(bg="lightblue")  # Cambia el color de fondo de la ventana a azul claro.

labelframe = tk.LabelFrame(ventana, text="Grupo de Widgets", bg="yellow", padx=10, pady=10)
labelframe.configure(width=300, height=200)
labelframe.pack()

ventana.mainloop()  # Inicia el bucle principal que mantiene la ventana abierta y responde a eventos.

# frame1 = tk.Frame(ventana)  # Crea un marco (frame) dentro de la ventana principal.
# frame1.configure(width=300, height=200, bg="red", bd=5)  # Establece el tamaño, color de fondo y borde del marco.
# frame1.pack() 

# frame2 = tk.Frame(frame1)
# frame2.configure(width=100, height=100, bg="blue", bd=5)

# boton = tk.Button(frame1, text="Hola")
# boton.pack()
# frame2.pack()


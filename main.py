import tkinter as tk 

ventana = tk.Tk()

ventana.title("Mi primera ventana")
#cambia las dimensiones de la ventana
ventana.geometry("600x400+0+0") #puedes modificar donde vas a colocar la ventana
#Configura la ventana para que no se pueda minimizar desde ciertos paramteros
ventana.minsize(400, 200)
#Pongamos ahora un tamaño máximo (para que no se pueda crecer la ventana a partir de ciertas dimensiones)
ventana.maxsize(800, 600)
#Llama el ícono que descargaste
ventana.iconbitmap("perrito.ico")
#Cambia el color de fondo de la ventana
ventana.configure(bg="lightgreen")
#se utiliza para configurar si la ventana puede ser redimensionada
ventana.resizable(False, True)
#Agrega transparencia a la ventana (opcional) siendo el valor 1 el 100%
ventana.attributes("-alpha", 0.9) 

ventana.mainloop()
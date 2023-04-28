# ----------------------------
# desktop app no. 1
# ---------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *

#  --------------------
# funciones de la app
# ---------------------

# ---------------------
# ventana principal
# ---------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()
# titulo de la ventana
ventana_principal.title("bandera de Colombia")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# desavilitar el botón de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg= "blue")

# -----------------------
# frame amarillo
# ------------------------
frame_amarrillo = Frame(ventana_principal)
frame_amarrillo.config(bg="yellow", width=500, height=250)
frame_amarrillo.place(x=0, y=0)

# -----------------------
# frame azul
# ------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=500, height=125)
frame_azul.place(x=0, y=250)

# -----------------------
# frame rojo
# ------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=150)
frame_rojo.place(x=0, y=375)
# run
# se ejecuta el metodo mainloop() de la clase Tk a travvés de la instancia ventana_principal. este metodo despliega la ventana en pantalla y queda a la espera de la que el usuario haga (click en un boton, escribir, etc). cada acción del usuario se conoce como evento. el méttodo mainloop() es un bucle infinito.
ventana_principal.mainloop()



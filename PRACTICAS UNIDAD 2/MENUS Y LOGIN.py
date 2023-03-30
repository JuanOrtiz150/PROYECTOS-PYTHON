# CODIGO PARA GENERAR UN MENÚ
# FECHA: 09/03/23
# AUTOR: JUAN CARLOS ORTIZ SALAS

import tkinter as tk


def Saludar():
    print("HOLA")


def open_file():
    print("ABRIR DOCUMENTO")


def take():
    op = usuario.get()
    print(op)


# VENTANA 2

def VentanaSecundaria():
    # Crear una ventana secundaria.
    ventana2 = tk.Toplevel()
    ventana2.title("MENU")
    ventana2.config(width=300, height=300)
    # Crear un botón dentro de la ventana secundaria
    # para cerrar la misma.
    boton_cerrar = tk.Button(
        ventana2,
        text="Cerrar ventana",
        command=ventana2.destroy
    )
    boton_cerrar.place(x=85, y=85)

# VENTANA 3


def VentanaTre():
    ventana3 = tk.Toplevel()
    ventana3.title("Nueva ventana")
    ventana3.config(width=500, height=500)
    boton1 = tk.Button(
        ventana3,
        text="CERRAR",
        command=ventana3.destroy
    )
    boton1.place(x=400, y=450)


# VENTANA 1

ventana = tk.Tk()
ventana.config(width=400, height=400)
ventana.title("Ventana principal")

# barra

barra_menus = tk.Menu()
menu_archivo = tk.Menu(barra_menus, tearoff=0)
ayuda_menu = tk.Menu(barra_menus, tearoff=0)

# Agregarlo a la barra.

barra_menus.add_cascade(menu=menu_archivo, label="Mensaje")
menu_archivo.add_command(label="hola", command=Saludar)
menu_archivo.add_command(label="Abrir Archivo", command=open_file)
barra_menus.add_cascade(menu=ayuda_menu, label="Nuevo")
ayuda_menu.add_command(label="Nueva ventana", command=VentanaTre)

ventana.config(menu=barra_menus)

# agregar entradas y mostrarlas

usuario = tk.Entry(ventana)
usuario.place(x=140, y=100)


# boton para abrir la ventana secundaria

boton_abrir = tk.Button(
    ventana,
    text="Hablar",
    command=take
)

boton_abrir.place(x=130, y=150)

ventana.mainloop()

# LOGIN USANDO BASE DE DATOS
# FECHA: 12/03/23
# AUTOR: JUAN CARLOS ORTIZ SALAS


import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql


# CREAR VENTANA PRINCIPAL***************************VENTANA 1


def saludo():
    print("HOLA")


def destruir():
    return ventanaAcceso.destroy()


def Acceso():
    global ventanaAcceso
    ventanaAcceso = tk.Tk()
    ventanaAcceso.title("VENTANA DE ACCESO")
    ventanaAcceso.geometry("500x400")
    Label(ventanaAcceso, text="HOLA, USUARIO", bg="navy", fg="white",
          width="300", height="3", font=("Calibri", 15)).pack()
    Label(ventanaAcceso, text="").pack()
    boton_cerrar = Button(
        ventanaAcceso,
        text="Cerrar",
        height="4",
        width="30",
        command=destruir
    )
    boton_cerrar.place(x=140, y=150)
    boton_salud = Button(
        ventanaAcceso,
        text="saludar",
        height="4",
        width="30",
        command=saludo
    )
    boton_salud.place(x=140, y=250)


def Principal():
    global ventana
    ventana = tk.Tk()
    ventana.title("Ventana principal")
    ventana.geometry("500x400")
    Label(ventana, text="IHOLA, ANTES DE INICIAR,", bg="navy", fg="white",
          width="300", height="3", font=("Calibri", 15)).pack()
    Label(ventana, text="").pack()

    boton_in = Button(
        ventana,
        text="Iniciar sesion",
        height="4",
        width="30",
        command=iniciarSesion
    )
    boton_in.place(x=140, y=150)

    boton_reg = Button(
        ventana,
        text="Registrarse",
        height="4",
        width="30",
        command=RegistroUsuario
    )
    boton_reg.place(x=140, y=250)

    ventana.mainloop()


def iniciarSesion():
    global pant1
    pant1 = tk.Toplevel(ventana)
    pant1.title("Iniciar sesion")
    pant1.geometry("500x400")

    Label(pant1, text="INICIO DE SESION", bg="navy",
          fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(pant1, text="").pack()
    Label(pant1, text="Usuario", bg="Cyan4",
          fg="white", width="40", height="3", font=("Calibri", 15)).pack()
    Label(pant1, text="").pack()
    Label(pant1, text="Contraseña", bg="Cyan4",
          fg="white", width="40", height="3", font=("Calibri", 15)).pack()

    # estas serviran para validar

    global usuario_verify
    global contrasena_usuario_verify

    usuario_verify = StringVar()
    contrasena_usuario_verify = StringVar()

    # estas son para dar la entrada del inicio de sesion

    global usuario_entrada
    global contrasena_entrada

    usuario_entrada = StringVar()
    contrasena_entrada = StringVar()

    usuario_verify = tk.Entry(pant1)
    usuario_verify.place(x=190, y=150)
    contrasena_usuario_verify = tk.Entry(pant1,  show="*")
    contrasena_usuario_verify.place(x=190, y=250)

    boton_iniciar = tk.Button(
        pant1,
        text="Iniciar sesion",
        command=ValidacionDatos
    )
    boton_iniciar.place(x=215, y=350)


def RegistroUsuario():
    global pant2
    pant2 = tk.Toplevel(ventana)
    pant2.title("Registrarse")
    pant2.geometry("500x400")

    Label(pant2, text="¿NUEVO USUARIO?, REGISTRATE", bg="navy",
          fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(pant2, text="").pack()
    Label(pant2, text="Usuario", bg="Cyan4",
          fg="white", width="40", height="3", font=("Calibri", 15)).pack()
    Label(pant2, text="").pack()
    Label(pant2, text="Contraseña", bg="Cyan4",
          fg="white", width="40", height="3", font=("Calibri", 15)).pack()

    global usuario2_entry
    global contrasena_usuario2_entry

    usuario2_entry = StringVar()
    contrasena_usuario2_entry = StringVar()

    usuario2_entry = Entry(pant2)
    usuario2_entry.place(x=190, y=150)
    contrasena_usuario2_entry = Entry(pant2,  show="*")
    contrasena_usuario2_entry.place(x=190, y=250)

    boton_registrar = Button(
        pant2,
        text="¡Registrarse!",
        command=IngresarDatos
    )
    boton_registrar.place(x=215, y=350)


def IngresarDatos():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bd1"
    )

    fcursor = db.cursor()

    sql = "INSERT INTO login (usuario, contrasena) VALUES ('{0}', '{1}')".format(
        usuario2_entry.get(), contrasena_usuario2_entry.get())

    try:
        fcursor.execute(sql)
        db.commit()
        messagebox.showinfo(message="REGISTRO ES EXITOSO",
                            title="AVISO DE REGISTRO")
    except:
        db.rollback()
        messagebox.showinfo(
            message="dou! No se pudo realizar el registro", title="AVISO DE REGISTRO")
    db.close()


def ValidacionDatos():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bd1"
    )

    fcursor = db.cursor()

    fcursor.execute("SELECT contrasena FROM login WHERE usuario='" +
                    usuario_verify.get()+"' and contrasena='"+contrasena_usuario_verify.get()+"'")

    if (fcursor.fetchall()):
        Acceso()
    else:
        messagebox.showinfo(title="INICIO DE SESION INCORRECTA",
                            message="EL USUARIO Y CONTRASENA NO SON CORRECTAS :/")

    db.close()


Principal()

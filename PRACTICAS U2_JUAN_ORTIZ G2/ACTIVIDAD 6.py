# LOGIN USANDO BASE DE DATOS, ASI COMO REGISTRO EN UN TREE CON BD, EN ESTE CASO SE UTILIZA EL MYSQL.CONNECTOR PARA LA BD, ES NECESARIO ENCENDER LA BD EN XAMPP PARA QUE EL PROGRAMA NO TENGA FALLAS
# FECHA: 12/03/23
# AUTOR: JUAN CARLOS ORTIZ SALAS


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


# CREAR VENTANA PRINCIPAL***************************VENTANA 1


def saludo():
    print("HOLA")


def destruir():
    return ventanaAcceso.destroy()


def Acceso():
    global ventanaAcceso
    ventanaAcceso = tk.Tk()
    ventanaAcceso.title("Ingresa tu comic/manga favorito")
    ventanaAcceso.geometry("500x400")
    Label(ventanaAcceso, text="Bienvenido, \n ingresa datos de tu comic/manga \n favorito", bg="navy", fg="white",
          width="300", height="3", font=("Calibri", 15)).pack()
    Label(ventanaAcceso, text="").pack()

    global manga
    global autor

    manga = StringVar
    autor = StringVar

    manga = tk.Entry(ventanaAcceso, font=("calibri", 12))
    manga.place(width=225, height=35, x=195, y=150)

    autor = tk.Entry(ventanaAcceso, font=("calibri", 12))
    autor.place(width=225, height=35, x=195, y=200)

    Label(ventanaAcceso, text="Obra: ", fg="grey1", width="12",
          height="2", font=("corbel", 12)).place(x=80, y=145)

    Label(ventanaAcceso, text="Autor: ", fg="grey1", width="12",
          height="2", font=("corbel", 12)).place(x=80, y=195)

    boton_guard = Button(
        ventanaAcceso,
        text="Guardar",
        height="4",
        width="30",
        command=tomar_obra
    )
    boton_guard.place(x=140, y=250)

    boton_most = Button(
        ventanaAcceso,
        text="Mostrar lista",
        height="2",
        width="30",
        command=music_list
    )
    boton_most.place(x=140, y=340)

    ventanaAcceso.mainloop()


def music_list():
    global ventanalista
    global lista_manga
    ventanalista = tk.Tk()
    ventanalista.title("Mangas/comics guardados")
    ventanalista.geometry("645x400")

    Label(ventanalista, text="Mis obras guardadas:", bg="navy", fg="white",
          width="65", height="2", font=("Calibri", 15)).place(x=0, y=10)

    boton_most = Button(
        ventanalista,
        text="Cerrar lista",
        height="1",
        width="15",
        command=ventanalista.destroy
    )
    boton_most.place(x=500, y=65)

    tabla_manga = LabelFrame(ventanalista, text=" Mis guardados ")
    tabla_manga.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
    tabla_manga.place(x=10, y=85)

    lista_manga = ttk.Treeview(
        tabla_manga, height=12, columns=("#1", "#"))
    lista_manga.grid(row=2, column=0, columnspan=1, padx=10, pady=5)

    lista_manga.heading("#0", text="ID", anchor=CENTER)
    lista_manga.heading("#1", text="Manga", anchor=CENTER)
    lista_manga.heading("#2", text="Autor", anchor=CENTER)

    consult_manga()


def Principal():
    global ventana
    ventana = tk.Tk()
    ventana.title("Ventana principal")
    ventana.geometry("500x400")
    Label(ventana, text="HOLA USUARIO", bg="navy", fg="white",
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
    db = mysql.connector.connect(
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
    db = mysql.connector.connect(
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


# ******PARA LA LISTA

def consult_manga():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="bdmanga"
    )

    fcursor = db.cursor()
    consulta = "SELECT * FROM lista ORDER BY id desc"
    fcursor.execute(consulta)
    datos = fcursor.fetchall()
    for i in datos:
        lista_manga.insert("", 0, text=i[0], values=(
            i[1], i[2]))


def tomar_obra():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="bdmanga"
    )

    fcursor = db.cursor()

    mga = "INSERT INTO lista (manga, autor) VALUES ('{0}', '{1}')".format(
        manga.get(), autor.get())

    try:
        fcursor.execute(mga)
        db.commit()
        messagebox.showinfo(
            message="Obra guardada", title="REGISTRO EXITOSO")
    except:
        db.rollback()
        messagebox.showinfo(
            message="No se pudo tomar el registro de la obra", title="AVISO SOBRE EL REGISTRO")
    db.close()


Principal()

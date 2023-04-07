# PRACTICA APLICANDO LAS PRIMERAS 4 ACTIVIDADES GUIADAS (LOGIN, MENU, BASE DE DATOS 1 Y REGISTROS EN UN BD)
# FECHA: 20/03/23
# AUTOR: JUAN CARLOS ORTIZ SALAS

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

# Iniciamos definiendo el login para ingresar una contraseña, para esto no usaremos una base de datos sino una contraseña ya preestablecida


def conectar_db():
    conexion = sqlite3.connect("playlist.db")
    conexion.execute("""
                create table if not exists lista(
                    id integer primary key AUTOINCREMENT,
                    nombre Varchar,
                    artista Varchar,
                    album, Varchar)
    """)
    conexion.close()


def guardar_cancion():
    conexion = sqlite3.connect("playlist.db")
    if music.get() == "" or artista.get() == "" or album.get() == "":
        messagebox.showerror("Error en los datos",
                             "Debe completar los datos del alumno")
        return
    conexion.execute(
        "insert into lista(nombre, artista, album) values (?,?,?)", (music.get(), artista.get(), album.get()))
    conexion.commit()
    conexion.close()
    ventana3.destroy()
    actualiza_listado()


def mostrar_playlist():
    conexion = sqlite3.connect("playlist.db")
    cursor = conexion.cursor()
    registros_raw = cursor.execute("select * from lista")
    registros_fetch = registros_raw.fetchall()
    print(registros_fetch)
    global registros
    registros = registros_fetch
    cursor.close()


def actualiza_listado():
    registros_lb.delete(0, tk.END)
    mostrar_playlist()
    for registro in registros:
        registros_lb.insert(tk.END, registro)


def validar():
    usuarioval = user1.get()
    contraval = contra1.get()

    if usuarioval == "juanortiz" and contraval == "admin":
        works()
    else:
        messagebox.showinfo(
            message="Inicio de sesion fallido, pista: \n juanortiz \n admin",
            title="Aviso")


def login():
    global ventana1
    ventana1 = tk.Tk()
    ventana1.title("Iniciar sesion")
    ventana1.geometry("700x500")

    Label(ventana1, text="Bienvenido de Nuevo", fg="midnight blue",
          font=("corbel light", 32)).place(x=165, y=60)
    Label(ventana1, text="Ingresa Usuario y Contraseña",
          fg="grey1", width="40", height="4", font=("corbel light", 15)).place(x=145, y=120)

    global user1
    global contra1

    user1 = StringVar()
    contra1 = StringVar()
    user1 = tk.Entry(ventana1, font=("calibri light", 12))
    user1.place(x=245, y=270, width=200, height=25)
    contra1 = tk.Entry(ventana1, show="●")
    contra1.place(x=245, y=300, width=200, height=25)

    boton1 = Button(ventana1,
                    text="OK",
                    font=("calibri light", 15),
                    bg="ghost white",
                    command=validar)
    boton1.place(x=245, y=330, width=200, height=50)

    ventana1.resizable(0, 0)
    ventana1.mainloop()


conectar_db()
mostrar_playlist()


def works():
    global ventana2
    ventana2 = tk.Tk()
    ventana2.title("Menu")
    ventana2.geometry("700x500")

    # Menus y toda la paranoia

    # Menu para aniadir las canciones y saludar al usuario

    barra_menus = tk.Menu(ventana2)
    menu_archivo = tk.Menu(barra_menus, tearoff=0)
    ventana_menu = tk.Menu(barra_menus, tearoff=0)

    barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
    menu_archivo.add_command(label="Añadir canción",
                             accelerator="Ctrl+N", command=add_song)
    menu_archivo.add_command(label="Imprimir un hola",
                             accelerator="Ctrl+H", command=hello)

    # Menu para ventana (cascada)

    barra_menus.add_cascade(menu=ventana_menu, label="Ventana")
    ventana_menu.add_command(label="tamaño chico (500x400)", command=ajustar1)
    ventana_menu.add_command(
        label="tamaño original (700x500)", command=ajustar2)
    ventana2.bind_all("<Control-h>", hello)
    ventana2.config(menu=barra_menus)

    # Tabla de datos de las canciones

    global registros_lb
    global registro

    registros_lb = Listbox(ventana2)

    for registro in registros:
        registros_lb.insert(tk.END, registro)

    registros_lb.place(x=100, y=100, width=400, height=300)

# Ahora añadimos las funciones de la base de datos para registrar y almacenar alumnos, asi como de funciones que realizara el menu


def ajustar1():
    ventana2.geometry("500x400")


def ajustar2():
    ventana2.geometry("700x500")


def hello(value: None):
    print("hola")


def add_song():
    global ventana3
    ventana3 = tk.Tk()
    ventana3.title("Agregar canciones")
    ventana3.geometry("500x400")

    global music
    global artista
    global album

    music = StringVar()
    artista = StringVar()
    album = StringVar()

    music = tk.Entry(ventana3, font=("calibri light", 12))
    artista = tk.Entry(ventana3, font=("calibri light", 12))
    album = tk.Entry(ventana3, font=("calibri light", 12))

    music.place(x=170, y=100, width=250, height=25)
    artista.place(x=170, y=150, width=250, height=25)
    album.place(x=170, y=200, width=250, height=25)

    Label(ventana3, text="Canción",
          fg="grey1", width="5", height="2", font=("corbel", 12)).place(x=95, y=94)
    Label(ventana3, text="Artista",
          fg="grey1", width="5", height="2", font=("corbel", 12)).place(x=95, y=144)
    Label(ventana3, text="Album",
          fg="grey1", width="5", height="2", font=("corbel", 12)).place(x=95, y=194)

    boton_save = Button(ventana3,
                        text="¡TODO LISTO!",
                        font=("calibri light", 15),
                        bg="ghost white",
                        command=guardar_cancion)
    boton_save.place(x=95, y=250, width=325, height=50)


login()
